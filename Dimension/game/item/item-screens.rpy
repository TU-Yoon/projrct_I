
# 인벤토리 영역을 어떻게 나타낼건지에대한 영역입니다.

define uses_gold = True
screen gold_count():

    frame xsize 500:
        align (.746,.682) padding (10,10)
        has hbox
        xfill True

        label _("돈")
        ##돈 이미지 추가 예정

        text "{}" .format(persistent.sit[2]) xalign 1.0

# 인벤토리 화면

default selected_item = None

# 아이템 설명
screen item_description(selling=False):
    frame xysize 1200, 100:
        align (.5,.80)
        padding (10,10,50,10)
        label _("설명") style "description_label" yanchor 24
        if selected_item is not None:
            $ thisitem = set_item(selected_item)
            text thisitem[3] offset (14,6) 
        elif selling:
            text _("아이템을 클릭하여 판매") offset (14,6) color "#8b8b8b"
        else:
            text _(" ") offset (14,6) color "#8b8b8b"

screen inventory(collection, selling=False):
    modal True

    #인벤토리 페이지 넘기기
    default first = 0
    default last = invgrid_x*invgrid_y
    default page = 1

    default sorted = False
    on "show" action SetVariable("selected_item", None)

    if uses_gold:
        use gold_count()

    # 화면 제목
    if selling:
        label _("상점") style "special_label" align (.1,.05)
    else:
        label _("인벤토리") style "special_label" align (.21,.25)

    style_prefix "inventory"

    # items
    use invgrid(collection, page, first, last)

    # page navigation
    hbox:
        xpos 385
        yalign .50
        spacing 532
        textbutton "<" ysize 256:
            sensitive first>0
            action [ SetScreenVariable("first", first-invgrid_x*invgrid_y), SetScreenVariable("last", last-invgrid_x*invgrid_y),
            SetScreenVariable("page",page-1) ]

        textbutton ">" ysize 256:
            sensitive len(collection)>last
            action [ SetScreenVariable("first", first+invgrid_x*invgrid_y), SetScreenVariable("last", last+invgrid_x*invgrid_y),
            SetScreenVariable("page",page+1) ]

    # sorting
    hbox:
        xpos 418
        yalign .33
        spacing 4
        style_prefix "sort"
        textbutton _("정렬 기준") text_color gui.idle_color

        textbutton _("이름"):
            if not sorted:
                action [Function(collection.sort, key=sortbyname), SetScreenVariable("sorted", True)]
            else:
                action [Function(collection.sort, key=sortbyname, reverse=True), SetScreenVariable("sorted", False)]

        if uses_gold:
            textbutton _("가격"):
                if not sorted:
                    action [Function(collection.sort, key=sortbyprice), SetScreenVariable("sorted", True)]
                else:
                    action [Function(collection.sort, key=sortbyprice, reverse=True), SetScreenVariable("sorted", False)]


    if selected_item is not None:
        $ thisitem = InvItem(*set_item(selected_item))
        frame xysize 500, 200: # 클릭시 나타나는 아이템 정보 창 사이즈
            xalign .746 ypos 320
            padding (10,10)

            label _("상세 설명") style "description_label" yanchor 24

            vbox pos (30, 20):
                spacing 10

                hbox ysize 96:
                    add thisitem.image at zoomx(2)

                    hbox xsize 260:
                        yalign 1.0 xfill True
                        text "x {}" .format(collection.count(thisitem.id)) xalign 0

                        if uses_gold and thisitem.value > 0:
                            hbox xsize 100:
                                xalign 1.0
                                text _("가격:")
                                text " {}" .format(int(thisitem.value/2))

                label thisitem.name style "special_small_label"

            vbox:
                align (.75,.2)
                style_group "sort"
                if selling:
                    textbutton _("팔기") action ShowTransient("buying", whichitem=thisitem, howmuch=thisitem.value, selling=True)
                else:
                    textbutton _("버리기") action [Function(thisitem.toss, 1), SetVariable("selected_item", None)]

    use item_description(selling)

    textbutton _("돌아가기") action Jump("My_home") style "offset_return_button" yalign .98

# gui 테투리 설정
style description_label_text:
    size gui.notify_text_size
    color "#fff"
    outlines [(1,"#000000",0,0)]
    bold True
style inventory_button:
    idle_background "#ffffff"
    hover_background "#686868"
    xpadding 12
style inventory_button_text:
    idle_color "#ffffff"
    hover_color "#474747" # 정렬 이름 버튼 글씨 색

style sort_button is inventory_button
style sort_button_text:
    idle_color "#9c9c9c"



# 아이템 아이콘 크기 조정
define itemslot_xysize = (52,52)

# 아이템 창 행과 열 조정
define invgrid_x = 10
define invgrid_y = 5

screen invgrid(collection, page, first, last, selling=False):

    frame:
        style "invgrid_frame"
        label _("아이템") style "description_label" xanchor 1000 yanchor 18

        # 항목 이름 표시
        $ tooltip = GetTooltip()
        if tooltip:
            label "[tooltip!t]" xalign 0.03 yalign 0.96

        grid invgrid_x invgrid_y:
            align (.5,.5) # 행, 열 위치조정
            # item buttons
            for item in collection[first:last]:
                if selected_item is not None:
                    $ thisitem = InvItem(*set_item(selected_item))

                button xysize itemslot_xysize:
                    style "itemslot_button"
                    add set_item(item)[1]
                    tooltip set_item(item)[0]

                    if selected_item==item:
                        if selling:
                            action ShowTransient("buying", whichitem=thisitem, howmuch=thisitem.value)
                        else:
                            action NullAction()
                    else:
                        action SetVariable("selected_item", item)


            for i in range(len(collection[first:last]), invgrid_x*invgrid_y):
                frame:
                    style "slot"

        text _("Page [page]") color gui.idle_color align (.96,.96)

style invgrid_frame: #인벤토리 창 상세 설정
    xysize (658,440)
    align (.35,.5)
    xoffset -80
style slot:
    background "empty_item"
    xysize itemslot_xysize
    xalign .5
style itemslot_button:
    background "[prefix_]item"
    padding (2,2)
    margin (0,0)
    size_group "inv"
    focus_mask True

style item_text:
    color "#FFF"
    outlines [(3,"#000000",0,0)]
    hover_outlines [(3,"#000000",0,0)]
style item_button_text:
    idle_color "#333"
style item_button:
    xsize 540
    ysize 52
    idle_background "#FFF"
    hover_background "#000000"

screen reward(itemdrop, get=True):
    zorder 100

    vbox at reward_appear:
        align (.5,.28)
        frame:
            add itemdrop at zoomx(2)
        if get:
            text "GET!" xalign .5 size 36

transform reward_appear:
    on show:
        alpha 0 yanchor -20
        easein_circ .5 alpha 1.0 yanchor 0
    on hide:
        linear .2 alpha 0.0 yanchor 10

transform zoomx(x):
    zoom x
    nearest True


style special_label_text:
    size gui.special_label_text_size
    bold True
    outlines [(3,"#4b4b4b",3,3),(2,"#fff",0,0)]
style special_small_label_text: # 타이틀 이름
    bold True
    outlines [(3,"#4b4b4b",2,2),(2,"#fff",0,0)] #상세 설명 글씨
style special_small_frame:
    background None
    xfill True

style offset_return_button:
    idle_background Frame("gui/button/choice_idle_background.png",100,5)
    hover_background Frame("gui/button/choice_hover_background.png",100,5)
    padding (100,5)
    xsize 340
    xoffset -80
style offset_return_button_text is choice_button_text:
    xalign 0

style go_button:
    idle_background "#8d8d8d"
    hover_background "#8d8d8d"
    insensitive_background "#a3a3a3"
    xysize (500, 100)
    align (.76,.9)
style go_button_text:
    size gui.special_label_text_size
    bold True
    xalign .5
    idle_color "#fff"
    hover_color "#fffba1"
    idle_outlines [(3,"#3d3d3d",1,1)]
    hover_outlines [(3,"#3a3a3a",1,1)]

style making_frame:
    xysize (500, 400)
    align (.5,.5)
    padding (30,30)
style making_button is go_button:
    xysize (400, 100)
    align (.5,.5)
style making_button_text is go_button_text



init -2:
    define gui.special_label_text_size = 32
