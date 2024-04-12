

screen recipes():
    style_prefix "craft"

    default page = 0
    default whichitem = InvItem(*set_item(known_recipes[0]))

    frame:
        style "craft_outer_frame"
        has vbox
        label _("제작") style "special_label"

        null height 20

        hbox:
        ##리셉션 사이드바 
            vbox:
                label _("레시피")

                # 레시피 카테고리 탐색
                if len(recipelists) > 1:
                    use recipenavi(page)

                # 레시피 버튼
                frame:
                    xysize (400, 450)
                    use recipelist(recipelists[page], whichitem)

            null width 40

        ##레시피 페이지
            frame:
                style "craft_content_frame"
                use recipeinfo(whichitem)

    # 아이템- screens.rpy의 하단에서 스타일을 변경할 수 있습니다
    textbutton _("Return") yalign .98 action Jump("test_menu") style "offset_return_button"


style craft_outer_frame:
    align (.5,.5)
    padding (40,20)
style craft_content_frame:
    xsize 700
    ysize 560
    ymargin 10
    padding (30,24)

style craft_button is inventory_button
style craft_button_text is inventory_button_text
style craft_viewport:
    xsize 280
style craft_side:
    spacing 10
style craft_vscrollbar:
    unscrollable gui.unscrollable
style craft_small_label_text:
    size gui.notify_text_size

screen recipenavi(page):
    # 표시할 레시피 목록 탐색
    frame:
        xalign .5
        has hbox
        xsize 392

        textbutton "<" xsize 44:
            if page==0:
                action SetScreenVariable("page", len(recipelists)-1)
            else:
                action SetScreenVariable("page", page-1)

        # 카테고리 라벨
        text recipelist_names[page] xalign .5 yalign .8 xsize 280

        textbutton ">" xsize 44:
            xalign 1.0
            if page==len(recipelists)-1:
                action SetScreenVariable("page", 0)
            else:
                action SetScreenVariable("page", page+1)

screen recipelist(whichlist, whichitem):
    # 실제 목록
    vpgrid style_prefix "recipe":
        cols 1 yfill True
        draggable True mousewheel True pagekeys True
        scrollbars "vertical"

        for i in whichlist:
            if i in known_recipes:
                $ thisitem = InvItem(*set_item(i))

                # 플레이어가 알고있는 레시피
                button:
                    action [ SetScreenVariable("whichitem", thisitem), Function(thisitem.see_recipe) ]
                    selected whichitem.id==thisitem.id

                    # 새로운 레시피에 마커 추가
                    if i not in seen_recipes:
                        foreground "itemmarker"
                    # 제작된 레시피에 대한 마커 추가
                    if i in made_recipes:
                        add "star"

                    # 본적이 있는 경우만 항목 추가
                    if i not in seen_items:
                        add thisitem.image + "2" alpha .3
                    else:
                        add thisitem.image

                    # 만들 수 있는지에 따라 색상 표시 변경
                    if check_ingredients(thisitem):
                        text thisitem.name
                    else:
                        text thisitem.name idle_color gui.idle_color

            # 모르는 
            else:
                button:
                    text _("????") color "#a7a7a7"

style recipe_button:
    xfill True
    ysize 48
    padding (0,0)
    idle_background "#fff"
    hover_background "#FFAFCF"
    selected_idle_background "#FFE8F1"
    selected_hover_background "#FFAFCF"
# style recipe_button_text:
    ## 텍스트 색상을 기본값으로 설정하지 않으려면 변경

style recipe_text:
    xoffset 48
    yalign .5
style recipe_label_text:
    bold True
    size 36

screen recipeinfo(whichitem):
    # 선택한 레시피의 항목 상세 내역을 보여주는 페이지
    vbox spacing 8:
        frame:
            style_group "special_small"
            has hbox
            xfill True
            label whichitem.name
            vbox:
                $ bagcount = inv.count(whichitem.id)
                $ craftcount = made_recipes.count(whichitem.id)
                align (1.0, 1.0)
                label _("In Bag: [bagcount]") style "craft_small_label" xalign 1.0
                label _("Crafted: [craftcount]") style "craft_small_label"

        $ tooltip = GetTooltip()
        hbox:
            if whichitem.id in seen_items:
                add whichitem.image at zoomx(2)
            else:
                add whichitem.image + "2" alpha .3 at zoomx(2)
            spacing 20

            vbox:
                null height 6
                label _("Ingredients:") style "craft_small_label"
                hbox:
                    style_prefix "itemslot"
                    spacing 5

                    # 재료를 단추로 나타냄
                    for i in whichitem.cost:
                        $ pr = InvItem(*set_item(i))
                        button:
                            # 본적이 있는 경우에만 항목에 이름 표시
                            if i in seen_items:
                                tooltip pr.name
                            else:
                                tooltip _("????")

                            action NullAction()

                            # 본적이 있는 경우에만 항목 이미지 표시
                            if i not in seen_items:
                                add pr.image + "2" alpha .3
                            else:
                                if inv.count(i) > 0:
                                    add pr.image
                                #인벤토리에 아무것도 없을 때 이미지를 빛바랜 것으로 표시
                                else:
                                    add pr.image alpha .3

                    if tooltip:
                        text "[tooltip!t]" style "making_text" xoffset 10 yalign .5

        frame:
            background None
            xfill True
            has vbox
            label _("Description:") style "craft_small_label"
            frame:
                background None
                text whichitem.info style "making_text"

    textbutton _("Synthesize..."):
        style "go_button"
        action ShowTransient("making", whichitem=whichitem)
        sensitive check_ingredients(whichitem)

screen making(whichitem):
    modal True

    add Solid("#f2cdd980")

    default amount = 1

    # 재고에서 만들 수 있는 최대 수를 계산
    $ maxcount = inv.count(whichitem.cost[0])
    for i in whichitem.cost:
        if inv.count(i) < maxcount:
            $ maxcount = inv.count(i)

    frame:
        style_group "making"
        # 재료의 수에 따라 창의 높이를 변경
        if len(whichitem.cost)==3:
            ysize 490
        else:
            ysize 440

        label _("Making...") style "description_label" anchor (20,44)
        vbox:
            yfill True
            frame:
                style_group "special_small"
                label whichitem.name
            null height 20

            # 항목 이미지를 사이에 두고 양을 선택하는 화살표 버튼
            hbox:
                style_prefix "inventory"
                ysize 48
                xfill True
                textbutton "<":
                    ysize 48
                    xalign 1.0
                    action SetScreenVariable("amount", (amount-1))
                    sensitive amount > 1
                    keysym "focus_left"

                hbox:
                    xalign .5
                    xoffset 40
                    if whichitem.id in seen_items:
                        add whichitem.image
                    else:
                        add whichitem.image + "2" alpha .3
                    fixed:
                        xsize 148
                        text _(" x [amount]") yalign .8

                textbutton ">":
                    ysize 48
                    action SetScreenVariable("amount", (amount+1))
                    sensitive amount < maxcount
                    keysym "focus_right"

            # 양을 1 또는 최대로 설정하는 단축키
            hbox:
                style_prefix "inventory"
                xalign .5
                spacing 20
                textbutton _("RESET"):
                    style "sort_button"
                    action SetScreenVariable("amount",1)
                    sensitive amount > 1

                textbutton _("MAX"):
                    style "sort_button"
                    action SetScreenVariable("amount", maxcount )
                    sensitive amount < maxcount

            null height 10

            # 필요한 재료와 몇 개를 사용할 것인지를 보여줌
            label _("Requires:") style "craft_small_label" xalign .15
            vbox:
                for i in whichitem.cost:
                    $ pr = InvItem(*set_item(i))

                    hbox xysize (420,48):
                        xfill True

                        hbox:
                            spacing 10
                            yalign .5
                            add pr.image
                            text pr.name yalign .5

                        hbox:
                            align (1.0,.5)
                            text "{}" .format(inv.count(i))
                            text " / [amount]"

                    null width 30

            # 물건을 만듬
            textbutton _("GO!"):
                action [ SetVariable("newitem", whichitem),
                    Function(whichitem.make, amount),
                    Jump("craft_success") ]

        textbutton "x" action Hide("making") keysym "game_menu" xalign 1.0 style "inventory_button"

# "making" 스타일은 아이템-screens.rpy의 맨 아래에 있습니다.
