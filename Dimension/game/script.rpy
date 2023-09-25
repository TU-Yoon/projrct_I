# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# live 2d 테스트 캐릭터
image me = Live2D("images/runtime", base=.6, loop = "true")



# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('매시안', color="#0C70F2")
define r = Character('리스', color="#D62124")




label process_quests:
    # add a quest with no unlock conditions
    $ add_new_quest("sucker3")

    # add a quest that only activates if you have money
    if new_quest("sugar1") and gold>0:
        $ new_quests.append("sugar1")

    # activate all new quests
    python:
        if len(new_quests) > 0: #if we have new quests
            for i in new_quests:
                active_quests.insert(0, i) #add to top of the quest list
            new_quests = [] #now reset the new quest list, since they all got added

##ITEMS
label inventory:
    scene home
    hide screen bag # 인벤토리 버튼을 숨깁니다.
    hide screen stat_overlay #스태미너를 숨깁니다.
    call screen inventory(inv) with Dissolve(.2)
    jump home

##CRAFTING
label start_crafting:
    scene bg lab
    call screen recipes() with Dissolve(.2)

label craft_success:
    show screen reward(newitem.image)
    "Made {color=#d48}[newitem.name!t]{/color}!"
    hide screen reward

    jump start_crafting

##QUESTS
label view_quests:
    scene bg lab
    call screen quests(page=0) with Dissolve(.2)

label activequest:
    call screen quests(page=0)
    jump s1

label completedquest:
    call screen quests(page=1)
    jump s1

## SHOP
label market_buy:
    scene bg shop
    call screen shop(market)
    jump s1

label market_sell:
    scene bg shop
    call screen inventory(inv, selling=True)
    jump s1


label start:
    python:
        gold = 20 #starting amount
        inv = []
        seen_items = []

        # crafting
        known_recipes = []
        seen_recipes = []
        made_recipes = []
        newitem = ""

        # shop inventory
        market = []

        # quests
        new_quests = []
        active_quests = []
        completed_quests = []

    $ InvItem(*item_pill).pickup(3)
    scene main_menu
    # 스태미너 창 보여주기
    show screen stat_overlay
    # 스태미너 창 숨기기
    #hide screen stat_overlay

    # 돈 1 증가
    # $ persistent.situation[2] += 1


    label test_menu:
    scene bg shop
    play music "bgm/Standby_screen.ogg"
    menu:
        "테스트를 위해 홈으로 갑니다.":
            jump My_home
        "스토리 테스트를 위해 스토리를 진행합니다.":
            jump s1

    label My_home:
    scene home
    show me hiyori_m01 #테스트 캐릭터
    show screen bag
    show screen stat_overlay
    # 돈 1증가
    $ persistent.sit[2] += 1
    $ some_condition = False

    "...."
    if some_condition:
        jump s1
    else:
        jump My_home




    label s1:
    # 배경
    scene p1
    "둥... 둥...."
    m "(여긴... 어디지.)"
    m "(눈을 떠보니 푸른 빛만 가득해. 그것 말곤 아무 것도 안 보여)"
    m "(....)"
    m "(여긴 아마, 천국으로 향하는 통로인 걸까)"
    m "(그럴지도. 난 그때 창으로 심장을 관통당하고 죽었으니)"
    m "난 '에리온' 이라는 세계에서 기사단의 단장으로 활동했었다. 1개월 밖에 안 됐지만."
    m "끝까지 살아남으면서 싸우고 병사들에게 본보기가 돼야 하는 직책일 터"
    m "단장으로서 좋은 모습을 보여줬어야 했는데. 그때 본보기가 되어주지 못했구나."
    m "지금 그들은 날 어떻게 생각하고 있을까."
    m "내가 천국으로 갈 자격이 있다고 여겼을까?"
    m ""

    return


    label s2:
    




    return


