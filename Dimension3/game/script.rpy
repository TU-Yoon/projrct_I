# 이 파일에 게임 스크립트를 입력합니다.
    # 돈 1증가
    # $ persistent.sit[2] += 1

    
# 게임 시작전 팀 로고를 불러옵니다
label splashscreen:
    $ renpy.movie_cutscene("images/splash.mpg")
    return


# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# live 2d 테스트 캐릭터
image me = Live2D("images/runtime", base=.6, loop = "true")
image sg = im.FactorScale("images/ch/reese/scg_reese_test.png", 0.5)


## 인벤토리 버튼 이벤트
label inventory:
    scene c2-2
    hide screen action_ui # 행동 버튼을 숨깁니다.
    call screen inventory(inv) with Dissolve(.2)
    jump home

## 액션 버튼 이벤트
label start_crafting:
    scene c2-2
    hide screen action_ui # 행동 버튼을 숨깁니다.
    call screen recipes() with Dissolve(.2)

label craft_success:
    show screen reward(newitem.image)
    "Made {color=#d48}[newitem.name!t]{/color}!"
    hide screen reward

    jump start_crafting

##퀘스트 버튼 이벤트
label view_quests:
    scene bg lab
    call screen quests(page=0) with Dissolve(.2)

label activequest:
    call screen quests(page=0)
    jump s1

label completedquest:
    call screen quests(page=1)
    jump s1

## 상점 이벤트
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
        inv = []
        seen_items = []

        # 제작 관련
        known_recipes = []
        seen_recipes = []
        made_recipes = []
        newitem = ""

        # 상점 관련
        market = []

        # 퀘스트 관련
        new_quests = []
        active_quests = []
        completed_quests = []


        ## 제작 / 상점 세팅
    $ known_recipes = ["item_sugar", "item_sucker"]
    
    ## 아이템 지급 알약
    $ InvItem(*item_telepathy).pickup(3)
    $ InvItem(*item_spicy_pork_cutlet).pickup(3)
    $ InvItem(*item_Random_machine).pickup(3)
    scene main_menu
    # 스태미너 창 숨기기
    #hide screen stat_overlay

    # 돈 1 증가
    # $ persistent.situation[2] += 1


    label test_menu:
    scene bg shop
    play music "audio/Standby_screen.ogg"
    menu:
        "테스트를 위해 홈으로 갑니다.":
            play sound "audio/sfx/click button.ogg"
            jump My_home
        "스토리 테스트를 위해 스토리를 진행합니다.":
            play sound "audio/sfx/click button.ogg"
            jump s1
        "테스트를 위해 점프 구간을 설정합니다":
            play sound "audio/sfx/click button.ogg"
            call input_jump_label


    label input_jump_label:
    $ jump_target = renpy.input("점프할 레이블 이름을 입력하세요: ")
    jump expression jump_target.strip()

    label action_menu:
    hide screen action_ui # 행동 버튼을 숨깁니다.
    # 상태창 GUI를 숨깁니다.
    python:
        hide_custom_guis()
    menu:
        "리스와 대화한다":
            play sound "audio/sfx/click button.ogg"
            jump chatgptmode
        "소지품을 확인한다":
            play sound "audio/sfx/click button.ogg"
            jump inventory
        "되돌아간다":
            play sound "audio/sfx/click button.ogg"
            jump re
        "스토리를 진행한다":
            play sound "audio/sfx/click button.ogg"
            jump story

    label re:
        if ret == 1:
            jump My_home1
        elif ret == 2:
            jump My_home2
        elif ret == 3:
            jump My_home3
        else:
            pass  # 다른 경우에 대한 처리

    label story:
        # $ st = 1  # st는 
    
        if st == 1:
            jump chapter1_1_c
        elif st == 2:
            jump chapter1_2_2_c
        elif st == 3:
            jump chapter1_2_3
        else:
            pass  # 다른 경우에 대한 처리

    label My_home:
    scene c2-2
    #show me hiyori_m01 #테스트 캐릭터
    show sg
    show screen action_ui
    # stat_overlay 스크린에 zorder를 설정해 가장 위에 표시
    show screen stat_overlay zorder 1
    $ some_condition = False
    "어디보자... 오늘은.."
    if some_condition:
        jump s1
    else:
        jump My_home



# 여기에서부터 게임이 시작합니다.
label s1:
    hide screen stat_overlay
    stop music

    #음악 수정(01prologue -> in the soul.ogg)
    play music "audio/music/in the soul.ogg"
    #fade -> slowfade로 수정
    scene p1 with slowfade  # 푸른빛의 공간
    #별 내리는 효과 추가(아래 4구문)
    image star1 = Fixed(SnowBlossom("gui/star1x.png", 40, xspeed=(20, 30), yspeed=(100, 200), start=5))
    image star2 = Fixed(SnowBlossom("gui/star2x.png", 40, xspeed=(20, 30), yspeed=(100, 200), start=5))
    show star1
    show star2

    ch_na "여긴... 어디지."
    "눈을 떠보니 푸른 빛만 가득해. 그 외엔 아무것도 안 보여."
    "여긴 아마, 천국으로 향하는 통로인 걸까."
    #아래 문장 수정(관통당했으니 -> 관통했으니)
    "그럴 지도. 그때 찔린 창이 내 심장을 관통했으니."
    "난 '에르온'이라는 세계에서 기사단의 단장으로 활동했었다. 비록 1개월 밖에 안 됐지만..."
    "단장으로서 좋은 모습을 보여줬어야 했는데, 그때 본보기가 되어주지 못했구나..."
    "지금 그들은 날 어떻게 생각하고 있을까. 내가 천국으로 갈 자격이 있다고 여겼을까?"

    #반짝이는 효과음 추가(flash.ogg)
    #eclipsy -> eclipsy2로 수정
    play sound "audio/sfx/flash.ogg"
    scene p1 with eclipsy2

    "독백하는 사이, 하얀빛이 세차게 뿜으며 내 눈앞을 감쌌다."
    "저게 곧 천국으로 간다는 신호겠지."
    "그래. 그곳에서라도, 부끄럼 없는 인생을 살며 보내야겠어."
    stop music fadeout 2.0
    jump s2




return