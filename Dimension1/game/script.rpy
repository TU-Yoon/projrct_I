# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# live 2d 테스트 캐릭터
image me = Live2D("images/runtime", base=.6, loop = "true")


## 인벤토리 버튼ㅇ 이벤트
label inventory:
    scene c2-2
    hide screen bag # 인벤토리 버튼을 숨깁니다.
    hide screen stat_overlay #스태미너를 숨깁니다.
    hide screen crafticon # 아이템 조합 창을 숨깁니다.
    call screen inventory(inv) with Dissolve(.2)
    jump home

##제작 버튼 이벤트
label start_crafting:
    scene c2-2
    hide screen bag # 인벤토리 버튼을 숨깁니다.
    hide screen stat_overlay #스태미너를 숨깁니다.
    hide screen crafticon # 아이템 조합 창을 숨깁니다.
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
    $ InvItem(*item_beet).pickup(3)
    $ InvItem(*item_telepathy).pickup(3)
    $ InvItem(*item_spicy_pork_cutlet).pickup(3)
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
    scene c2-2
    show me hiyori_m01 #테스트 캐릭터
    show screen bag
    show screen stat_overlay
    show screen crafticon
    # 돈 1증가
    $ persistent.sit[2] += 1
    $ some_condition = False

    "...."
    if some_condition:
        jump s1
    else:
        jump My_home


# 여기에서부터 게임이 시작합니다.
label s1:
    scene p1 with fade  # 푸른빛의 공간

    ch_na "- 둥... 둥... "
    "여긴... 어디지."
    "눈을 떠보니 푸른 빛만 가득해. 그 외엔 아무것도 안 보여."
    "여긴 아마, 천국으로 향하는 통로인 걸까."
    #아래 문장 수정(관통당했으니 -> 관통했으니)
    "그럴 지도. 그때 찔린 창이 내 심장을 관통했으니."
    "난 '에르온'이라는 세계에서 기사단의 단장으로 활동했었다. 비록 1개월 밖에 안 됐지만..."
    "단장은 끝까지 살아남아 싸우고 병사들에게 본보기가 돼야 하는 직책일 터."
    "단장으로서 좋은 모습을 보여줬어야 했는데, 그때 본보기가 되어주지 못했구나..."
    "지금 그들은 날 어떻게 생각하고 있을까. 내가 천국으로 갈 자격이 있다고 여겼을까?"

    #[빛이 하얗게 뿜어지는 연출]
    #flash = 반짝이는 연출
    define flash = Fade(2, 0, .75, color="#fff")
    scene p1 with eclipsy
    "독백하는 사이, 하얀빛이 세차게 뿜으며 내 눈앞을 감쌌다."
    "저게 곧 천국으로 간다는 신호겠지."
    "그래. 그곳에서라도, 부끄럼 없는 인생을 살며 보내야겠어."

label s2:
    scene p2 with flash  # 어느 산속
    
    ch_na "눈을 떠보니, 새들의 울음소리와 동시에 태양이 내리쬐는 산속이었다."
    "이곳이 천국인가. 내가 살았던 세계와 비슷해 보이는데."
    "아니면 천국으로 향하는 입구일지도 모르겠지." 
    "새로운 인생도 익숙한 장소를 시작으로 서서히 미련을 버리면서 가는 거잖아."

    #잠시 대기하는 연출 추가(scene p2 pause 0.3 scene p2)
    scene p2 
    pause 0.3
    scene p2
    "-스르륵."
    "어라? 몸을 살짝 움직였더니..."
    "아, 몸에 뭔가 걸쳤구나." 
    "긴 검은 셔츠에 남색 바지, 회색 장갑, 그리고 모델이 입을 것 같은 하얀 코트까지 있네."
    "전체적으로 꽉 끼지도 않고 헐렁하지도 않고, 적당해. 죽기 전에 입었던 옷과는 확실히 달라."
    "내가 갑자기 왜 이걸 입었는지 의아하긴 하지만... 그래도 알몸으로 있지 않은 게 어디냐."
    "그건 그렇고, 일단 여기가 뭐 하는 곳인지는 알아봐야겠지."
    "어디 구경할 만할 데가 있나."


label s3:

    #dissolve : 장면을 자연스럽게 전환할 때 상용
    scene p3 with dissolve # 부산 시장가

    ch_na "터벅... 터벅..."
    "산 속에서 빠져나오니, 시장처럼 보이는 골목이 나왔다."
    "상점들이 빼곡하게 자리 잡고 있었고, 사람들이 와글대며 골목을 거닐고 있는 걸 보면 인기가 많은 곳인가 보다."
    "이곳저곳에서 물건을 사고파는 상황들로 가득하니 여기가 천국에서 잘나가는 시장 중 하나겠지."
    "그건 그렇고, 이곳에 왔으면 일단 뭐부터 해야 하지?"
    "아, 그래. 여기도 입국 허가 절차 같은 게 있을 거야."
    "일단 공항으로 가야겠다. 정식으로 입국 신고를 해야 천국 사람이라고 인정받을 수 있을테니까."
    "저기 생선을 파시는 아줌마한테 한 번 물어봐야지. 여기에 대해서 잘 아실 테니 말이야."

    #선택지
    menu:
        "선택지 1 : OOOOOOOO?":  #&@^%&%^이 원래 대사인데 넣으면 오류가 나서 임시로 영어를 넣어두었습니다.
            m "실례합니다. 공항으로 가는 길이 어딘지 여쭤봐도 될까요?"
            jump s3_1

        "선택지 2 : OOOOOOOO?":  #*&^@*^*@ 마찬가지로 오류
            m "생선이 참 튼실하네요! 천국 바다에서 잡은 생선 맞죠?"
            jump s3_1

label s3_1:

    fish "응?" #fish = 생선 아줌마
    ch_na "으음... 표정이 황당해 보이시는데. 내 말을 알아듣지 못하신 건가."
    fish "뭐라카노? 다시 한 번 말해뿌라."
    m "sadks?   (네?)"
    #아래 2개 문장 분리
    "저게 대체 뭔 소리야. 나도 저 사람의 말을 못 알아듣겠는데?" 
    "천국에서 따로 사용하는 언어가 있는 건가."
    "이거 어떻게 풀어나가야... 아, 그래! 바디랭귀지를 한 번 시도해보자."

    #잠시 대기하는 연출 추가(scene p3 pause 0.2 scene p3)
    scene p3
    pause 0.2
    scene p3
    "-휙. 휙."
    "난 하늘을 가리키고 비행기처럼 날개를 펼쳐 나는 시늉을 보였다."
    "허접하면서도 수치스럽긴 하지만, 어쩌겠어. 일단 이렇게라도 대화해야 길이 트이잖아."
    fish "...아! 니, 외국인이었나?"
    #대사 추가("가만 있자. 정류장이 분명...")
    fish "가만 있자. 정류장이 분명..."
    # 동작 단어 삭제('-스윽.')
    ch_na "다행히도 아줌마가 알아들으신 모양인지, 손가락으로 어딘가를 가리키셨다."
    fish "저그서 오는 버스를 타고 쭉 가믄 공항이 보일 기다. 거그서 내리면 된다."
    m "oipjh, dfghjl!  (그렇군요, 감사합니다!)"

    "가리키신 곳이 버스 정류장이었구나. 저기서 버스를 타면 되겠지?"
    "어디 보자, 정류장에 붙은 노선도를 보면... 그래, 저 번호가 적힌 버스를 타면 공항으로 갈 수 있겠구나."


label s4:
    scene p4 with dissolve # 버스 장면

    "-끼익."
    "잠시 기다린 사이, 전광판에 307이라고 적혀있는 버스가 도착했다."

    "저 버스가 공항으로 간다고 노선도에 적혀있었으니 저걸 타면 될 거야."

    #잠시 대기하는 연출 추가(scene p4 pause 0.3 scene p4)
    scene p4 
    pause 0.3
    scene p4
    "- 삐~"
    "신호음과 동시에 버스 문이 열리자, 먼저 안에 올라타 자리에 앉으려 했다."

    #bus = 버스 기사
    bus "저기, 손님!"
    #아래 문장 수정 & 분리
    ch_na "뭐야, 기사님이 갑자기 나를 보며 소리치시네."
    "내가 뭘 잘못한 게 있나, 왜 그러시는걸까?"
    bus "그냥 타시면 안 돼요!"
    ch_na "정말이지. 말이 안 통하니까 문제를 어떻게 해결해야 할지 모르겠네."
    #아래 문장 수정
    "일단 기사님을 만나러 가봐야 되겠다. 무슨 의도로 말하는 지 알아먹어야 하잖아."

    #잠시 대기하는 연출 추가(scene p4 pause 0.2 scene p4)
    scene p4 
    pause 0.2
    scene p4
    "-스윽."
    "직접 대면하자, 기사님이 작은 모니터가 달린 기기와 돈을 넣는 투입구를 가리키셨다."
    #아래 문장 수정("저기에" -> "저기다")
    bus "저기다 카드를 찍으시거나 여기 안에 돈을 넣으시고 타셔야죠."
    ch_na "아, 맞다. 왜 버스 요금을 생각 못했지."
    #아래 문장 수정("누군가한테" -> "누구한테")
    "근데 돈을 무슨 수로 내야 하나. 나 지금 한 푼도 없는데, 지금 당장 누구한테 빌려야 해?"
    "안돼, 그럴 수는 없지. 그냥 걸어가는 수밖에."
    "힘들겠지만 양심을 버리고 멋대로 탈 수는 없잖아."

    mys "아, 저기..."

    "버스에서 내리려 마음먹던 순간, 어떤 청년이 버스 기사에게 말을 걸었다."

    bus "아는 사이이신가요?"
    mys "친구가 먼저 정류장에 자리를 잡고 있어가지고, 하하핫..."
    bus "아아, 알겠습니다."
    ch_na "뭔 상황인지 모르겠지만, 일단 내려야겠지? 나랑은 상관없는 일이잖아."
    bus "손님! 타셔도 돼요!"
    ch_na "뭐야, 갑자기 기사님이 안으로 들어오라는 손짓을 하네. 타도 되는 거야?"
    bus "저분이랑 아는 사이 아니셨어요?"

    ch_na "버스 기사가 방금 요금을 낸 남자를 가리켰다." 
    "설마 저 남자가 내 버스비까지 내 준건가?"
    "-휙휙."
    "남자도 들어오라고 손짓을 한 걸 보면 정말 내준게 맞나 보다."
    "그럼... 타도 별문제 없겠지?"

    #잠시 대기하는 연출 추가(scene p4 pause 0.2 scene p4)
    scene p4 
    pause 0.2
    scene p4

    "-부우우웅."
    "자리에 앉음과 동시에, 버스가 요란한 소리를 내며 출발했다."

    #아래 두 문장 분리
    "일단 저 남자 덕분에 어찌저찌 타기는 했네."
    "감사 인사라도 전하고 싶지만, 말이 안통하니 그럴 수가 없겠구만..."
    "입국 허가를 받고 난 다음에는 바로 언어를 배울 수 있는 학교로 들어가야겠다."
    "나중에 다시 만나기라도 한다면 감사 인사를 전할 수 있을지도 모르지. 여기에 대해서 잘 아실 테니 말이야."


label s5:
    scene p5 with dissolve  # 공항

    ch_na "-끼익."
    "버스는 달리고 달려서 어느덧 공항으로 보이는 건물에 도착했다."
    "버스에서 내린 뒤 주위를 살펴보며, 내가 생각한 곳과 맞는지 분석해보았다."
    #아래 두 문장 분리
    "근처에서 비행기가 이륙하는 소리."
    "캐리어를 끌고 안으로 들어가는 다양한 인종의 사람들..."

    "그래, 확실히 공항인 것 같다. 조금 전 노선도로 봤을 때도 이 정류장에 비행기 마크가 붙어 있었잖아."
    #아래 두 문장 분리
    "좋아, 본격적으로 부딪혀볼까."
    "들어가서 후딱 끝낸 다음에 새로 터전을 찾으러 궁리해보자고."

    scene p5 with eclipsy #눈이 하얘지는 연출

    "윽, 뭐야! 갑자기 눈이 왜 하얘져..."
    "목이 갑자기 조이고 있는 느낌이 들었다. 누가 이러는 거지?"
    m "콜록, 콜록!"
    with Shake((0, 0, 0, 0), 0.4, dist=30)
    ch_na "계속 목이 졸리는 고통 속에, 나는 주저앉고 말았다."
    "호흡은 쉴 새 없이 가빠지고, 정신은 아늑해져 가고..." 
    "설마, 나 또 죽는 거야? 여기 온 지 얼마 됐다고?"
    "으으, 눈이... 점점 감긴다. "
    "천국에서 죽으면 난 대체 어디로 가는 거야..."




label s6:
    #eyeclose에서 eyecloseslow로 변경
    scene p6 with eyecloseslow

    mys "정신이 드나?"

    ch_na "서서히 의식이 다시 깨어나려 할 때, 소녀로 추정되는 목소리가 귓가에 들렸다."
    "여전히 무슨 말을 하는지 알 수는 없었지만, 그녀가 날 병원으로 데리고 온 건가?"

    #눈을 뜨는 연출
    # 리스 평상 시 -> scg_reese normal
    show scg_reese normal with dissolve

    "그 목소리에, 나는 눈을 떴다."
    "근데 여기는 병원이 아닌데? 세련되면서도 고급져보이는, 귀족들이 지낼 것 같은 공간이잖아."
    "기절한 사이에 대체 무슨 상황을 겪은 거야, 난..."
    "붉은 양갈래 머리에 검붉은 고스로리 드레스..."
    "제법 화려한 차림을 한 듯한 소녀는 날 계속 응시하며 중얼거리고 있었다."
    "정체가 뭐지? 왜 나를 이곳으로 옮긴 거야?"
    m "etd... srw?(당신은... 누구죠?)"
    mys "응? 희한하구마. 에르온에서 쓰는 말을 다 하고."
    ch_na "내가 소녀의 정체가 뭔지 물어보고 싶어도 대화가 안 통하네, 대화가."
    "이런 말을 꺼내는 내가 바보지."

    mys "후우..."

    # 리스 평상 시 걸을 때 -> scg_reese normal walk
    show scg_reese normal walk with dissolve

    "검은 구두 소리와 함께, 소녀가 자기 손가락에 입김을 불며 나한테 다가왔다." 

    hide scg_reese normal walk 
    with dissolve
    "무슨 의도로 오는 건지 모르니까 부담스러운데..."

    with Shake((0, 0, 0, 0), 0.4, dist=30)



    "-빠악!!"

    "아얏! 뭐야, 갑자기 내 이마에 왜 딱밤을 때리는 거지? "
    "이해가 안 가는 짓을 하네? 아으, 가뜩이나 머릿속이 복잡해 열날 지경인데."

    show scg_reese normal with dissolve
    mys "마, 인자 내 말을 알아듣것제?"
    "어라, 갑자기.., 귀가 맑아진 느낌이 들어. 이제 저 소녀의 목소리도 똑바로 들리고."
    "딱밤을 맞아서 그런가, 아님 내가 그 동안 정신을 못 차린 건가..."

    mys "여그 말을 알아들을 수 있도록 마법을 걸었다카라. 동시에 니 말도 한국어로 들리게 해줬고. "
    m "한국어요...?"
    mys "기래, 한국에서 쓰는 언어다카라."

    #[화면이 흔들리는 연출]
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m " ...에에에에?!"

    m "천국이 아니라 한국이라고? 잘못 들은 거지, 내가?
    사후 세계가 천국과 지옥말고 다른 데가 어디 있겠어?"

    mys "와 그리 놀라나?"
    m "혹시, 천국이라고 말씀하셨나요? 제가 말을 잘 못 알아 들어갖고..."
    mys "천국? 니, 가톨릭 신자가?"
    m "가톨릭? 이건 또 무슨 말이야. 신자라고 하는 걸 보면 종교 쪽인 것 같은데."
    m "그럼 여기가... 천국이 아니에요?"

    # 리스가 황당할 때 -> scg_reese confuse
    show scg_reese confuse with dissolve

    mys "뭔 소리를 하는 겨. 니 설마 사이비 놈들헌테 홀린 건 아니제?"
    m "저, 저 종교 안 믿어요! 사이비도 안 믿고요!"
    ch_na "흐아... 머리가 점점 해탈해져 간다..."
    "천국도 아니고, 에르온도 아니고, 여긴 어떤 세계인 거지?"

    show scg_reese normal with dissolve
    mys "여긴 천국이 하니라 한국이다. 풀어서 말허믄, 대.한.민.국이라고 혀지. 알아듣것나?"
    "한국이건 대한민국이건 간에 지금 그게 문제가 아니다."
    ch_na"나 분명 죽었을텐데. 심장 뚫려서 뒤졌잖아."
    "그럼 내가 있을 곳은 천국 아니면 지옥 아니야? 여긴 누가 있는 땅인데!"
    mys "암튼, 여그는 처음이라 아직 적응이 잘 안 되제? 조만간 적응하믄, 괜찮아 질 기라."
    ch_na "말은 괜찮다고 했는데, 원치도 않은 세계에서 발을 디뎠는데 지금 괜찮을 수가 있겠냐고..."
    "...일단 진정하자. 저 소녀한테 감사의 말부터 올려야지."
    m "아아, 네. 감사했습니다. 덕분에 잘 적응할 수 있을 것 같아요."

    ch_na "일단 여기서 물러나 앞으로의 계획부터 짜보자고. 내가 왜 여기 있는지부터 알아야 하니까."

    show scg_reese smile with dissolve
    mys "감사혀야제. 앞으로 더 감사혀야 할 일이 많을 끼니."

    ch_na"자, 잠깐... 불안하게 그건 또 갑자기 무슨 말이야."
    "저 소녀가 나한테 볼 일이 또 있는 모양인건가?"
    mys "잘 들으라. 그대는 이제부터..."
    ch_na "소녀의 손가락이 나를 향하며 내게 명령하듯이 말하는데... 가만."
    "이거 설마, 아니겠지? 제 입맛대로 부려먹는 그런 쪽이 아니길 바래야..."
    mys "내 집사가 되는 기라!"

    ch_na "..."

    "...아."

    #프롤로그 종료(챕터 종료 시 scene black with eyecloseslow)
    scene black with eyecloseslow



#[챕터 1-1]

label chapter1_1:
    scene c1-1 with dissolve   #리스의 집
    
    m "...ㄴ, 네?!"
    ch_na "정말 어처구니가 없네. 방금 저 소녀가 한 말이 뭐라 했냐, 날 집사로 만들겠다?"
    "가만히 생각해보니까 쟤가 하는 말 하나하나가 믿기지를 않네. 무슨 말도 안 되는 소리를 자꾸 하는 거야, 저 애는." 
    "천국이 아니라 다른 세계라 그러고. 갑자기 날 집사로 부려 먹는다고 하고."
    #아래 두 문장 분리
    "정신이 아득해지는 건 둘째치고, 내 인내심에 자꾸 불을 붙이려 하네?"
    "초면인 상대에게 그런 부담스런 말을 하는 것도 정도가 있지."

    show scg_reese normal with dissolve

    mys "니는 이제부터 내 집사라고. 알아들읏나?"
    m "무슨 소리를 하시는 거예요! 왜 제가 당신의 집사가 되어야..."
    mys "자세한 얘기는 나중에 한다카라. 일단은..."
    #아래 두 문장 분리
    m "일단은! 이유부터 말씀해주셔야 제가 납득이 가든가 하죠!"
    m "이렇게 나 몰라라 발뺌하시면..."
    # 리스 화날 때 -> scg_reese angry
    show scg_reese angry with dissolve
    #아래 두 문장 분리 및 수정
    mys "발뺌? 으디서 철이 덜 든 소리를...!"
    mys "이 자슥아, 나가 니 같은 사람 붙잡고 평생 노예처럼 부리먹는 줄 아나?"
    ch_na  "이거 거의 노예계약 아니야? 맞잖아. "
    "이 여자, 날 구해준 게 아니라 붙잡은 거네! 어쩐지 왜 여기로 왔나 했더니..."
    "얼른 여기서 벗어나야지. 저 사람이랑 붙었다가는 평생 고생길을 면치 못할 거야."
    mys "한 번 도망쳐봐라. 소용 읎는 짓이긴 하겠지만은."

    #아래 두 문장 분리 및 효과 추가
    m "뭐가 소용이 없..."

    # 구속 마법에 걸린 연출(shake 효과 적용)
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "윽!"

    ch_na "제기랄, 몸을 겨누려 하는데 움직이지를 않잖아. 정신을 잃은 동안 저 소녀가 저주라도 걸은 건가?"
    show scg_reese normal with dissolve
    mys "니한테 구속 마법을 걸었으니, 발뺌할 생각은 마라. 이 근방에서는 어디 있는지 다 알 수 있으니."
    ch_na  "구, 구속 마법?! 그럼 날 사방에서 감시하겠다는 소리잖아!"
    "젠장, 재수 옴 붙었구만. 하필이면 왜 저런 악덕 같은 사람한테 거두어졌느냐고...!"
    # 리스가 황당할 때 -> scg_reese confuse
    show scg_reese confuse with dissolve
    mys "방금 행동을 보니 내 집사가 되는 게 별 관심이 읎는 모양이구마."
    m "이유를 말씀해주시질 않으시니 그런 생각을 할 수밖에 없잖아요! 말씀해보세요, 제가 왜 당신 밑으로 들어가야 하는..."

    #[화면이 흔들리는 연출]
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    ch_na "-빠악!" 
    
    ch_na "내가 이유를 물으려고 하니 다시 딱밤을 불날 듯이 때리네, 아파라..."
    mys "가마이 있으라. 증말이지 말해줄 때가 있다고 처음에 한 번, 조금 전에 또 한 번 말했는디, 와 이리 고집부리나?!"
    m "아, 알겠습니다..."
    ch_na "일단 저 사람의 말을 들어야 할 것 같네. 이 이상 들이대도 도저히 말이 통하지 않을 거야."

    show scg_reese normal with dissolve


    mys "주종 관계로서 정식으로 인사를 올려야긋제? 내 이름은 사투 리스. 뱀파이어 혈통으로 이루어진 사투 가문의 귀족인기라."
    #아래 두 문장 분리
    ch_na "사투, 리스..."
    "그렇다. 사투리스는 뱀파이어다."
    r "그쪽 이름과 나이는 어케 되나?"
    m "매시안 크리스토프라고 합니다. 25살이고요."
    r "그렇구마... 예상은 혔지만, 딱 봐도 내랑 나이가 별 차이는 읎네."
    ch_na "그럼 이 소녀도 나랑 같은 성인인 건가? 체형이 제법 있는 걸 봐선 그럴 지도..."
    m "실례지만, 혹시 나이가 어떻게..."
    r "20살인기라. 인자 성인이 된 기분이 막 드는 나이제."

    ch_na "20살이라고 한다면 성인이잖아? 그럼 술도 마시고 하겠구만."

    #여기까지 수정 완료

    "나중에 잔뜩 취하거나 한다면 뒤처리도 해야 하고... "

    r "자, 통성명도 마쳤으니 인자 가사 활동을 시험혀보도록 허자."
    m "가사... 활동이요?"
    r "기래. 집사가 됬으믄 집안일 실력이 으뜬지 한 번 봐야하니께."

    ch_na "마, 맞는 말이긴 하지, 집사는 주로 가사 활동에 충실해야 하니까. 고된 시간이 되겠네."
    r "먼저 요걸로 성 안에 있는 모든 먼지를 다 쓸어뿌라. 말 잘 듣는 놈이니 안 빨릴 거란 걱정은 말고."
    ch_na "리스가 내게 건네준 건 T자형으로 생긴 무선청소기였다."
    "이걸로 쓸면 손잡이가 있는 쪽으로 먼지가 모이는 거겠지. 그쪽 부분에 먼지통 같이 생긴 게 있으니까."
    "근데 이 넓은 데를 나 혼자 쓸으라고? 합해도 한 60평은 넘어 보이는데, 여기?"
    r "와 그리 놀라나? 무슨 문제라도?"
    m "다, 당연하죠! 이 넓은 데를 어떻게 혼자서..."
    r "또 맞아야 정신을 차리것네."
    m "아, 번복할게요! 당연히 할 수 있죠! 헤헤..."
    r "...정신 좀 차리라, 이래가지고 집사 일을 어떻게 하긋냐?"
    ch_na "한숨이 절로 나올 것 같지만, 이 이상의 독설을 듣기는 무리니까..."

    #선택지
    menu:
        "선택지1 : 후딱 끝내자.":  
            jump chapter1_1_a

        "선택지2 : 힘 좀 들겠지만 꼼꼼하게 끝내는 게 좋겠지. (스테미나 -3)":  # 스테미나 -3
            jump chapter1_1_b

label chapter1_1_a: # 후딱 끝내자
    ch_na "보이는 것만 쓸고 끝내는 게 낫겠다. 혼자서 이 넓은 데를 어떻게 꼼꼼히 보겠어."
    "어디 보자, 먼지가 제일 많이 생길 만한 곳이... 그래, 이쪽이랑 저쪽만 인지하면 되겠다."
    "옷장이나 냉장고 근처는 신경 쓰기 힘들겠지. "
    "옷 갈아입어야 하고, 음식 꺼내야 하고... 먼지를 어케 신경 쓰겠니. "
    "-위이이잉~" # [청소기 효과음]
    "쓸면서 보니까 그리 먼지가 많이 보이지도 않네. 내가 너무 호들갑을 떨었나?
    금방 끝낼 것 같은 느낌이 드네. 좋아!"

    "- 약 1시간 뒤 -"

    m "후우..."
    ch_na "끝났다. 대청소의 대장정이 드디어 막을 내렸다."
    "이제 한숨 푹 돌려도 되겠지."
    r "다 했나?"
    m "끝났어요! 퍼펙트하게요!"
    ch_na "감이 왔다. 이건 무조건 합격이다."
    "적어도 이걸로 불평들을 일은 무조건 없을 거란 징조가 왔지."
    r "증말 니 말대로 퍼팩트하게 다 됐는지 한 번 볼까?"
    ch_na "리스가 청소했던 부분을 꼼꼼히 살피기 시작했다."
    "백날 찾아봐라. 먼지가 한 톨이라도 보이겠냐?"
    r "마, 집사!!"
    ch_na "어라? 리스가 날 바라보는 눈빛이 예사롭지 않네..."
    "뭔가 문제라도 있나?"
    r "퍼펙트는 무슨 얼어죽을! 여그 청소가 똑바로 안 됐잖나! 눈 똑바로 뜨시고 한 그 맞나?!"
    ch_na "엥? 분명히 쓸었던 곳에 왜 먼지가 쌓여 있지? 내가 눈이 좀 어두웠나?"
    m "분명 청소했던 곳인데..."
    r "구라치지 마라! 여그도 저그도 다 보이는디! 대충대충 혀면 나가 그냥 넘어갈 줄 알앗나?!"
    ch_na "실수가 좀 있었구만. 피땀 흘려가면서 미친 듯이 쓸었는데..."
    "...뭐, 대충 한 대가는 쓰다, 써. 생각 외로 꽤 꼼꼼하네." 
    "아님 내가 멍청했을지도. 변명이 오히려 독이 된 꼴이야."
    m "...눈깔을 굴리는 훈련이 부족했나 봅니다."
    ch_na "잘못을 범한 내게 해야 할 행동은 고개를 숙여 사과하는 것이었다."
    "그 이외의 선택지는 전무하니까."
    r "인자 주방으로 와보라. 요리를 한 번 볼 티니."
    jump chapter1_1_2

label chapter1_1_b: # 꼼꼼하게 끝내자
    ch_na "그래, 내가 청소 경력이 얼마나 되는데 이깟 거 못하겠냐."
    "각오해라, 먼지들아! 용병 시절 수 년간 겪었던 청소 경험으로 너희를 모두 쓸어버릴테니!"
    "-위이이잉~" # [청소기 효과음]
    "난 무선청소기의 전원을 켜 각 방과 거실, 주방 등 고성 곳곳을 쓸기 시작했다."
    "한 톨의 먼지도 보이지 않도록 안 보이는 데까지 꼼꼼하게! 잘 안 쓸리는 먼지가 있다면 걸레로 한 번 닦아주고!"
    "그, 근데 몸이 예전같지가 않네. 방금 허리를 삐끗할 뻔했어..."

    "- 약 1시간 뒤 -"

    r "으음... 뭔 꼼수라도 부린 기가, 안 보일 리가 없는디..."
    ch_na "아직 내 청소 실력을 인정하지 못한 모양이구만."
    "현미경을 써도 소용없어요. 그 전에 내가 청소 점검을 몇 번이나 했는데."
    r "크, 크흠... 잘혔구마. 의외로 그런 구석이 있을 줄은 몰랐는디."
    ch_na "꼼꼼한 면은 집사의 필수사항 아니겠어."
    "뭐, 내가 아직 이런 직종을 잘 모르긴 하지만. 틀린 말은 아니지. " 
    r "좋아, 인자 주방으로 와보라. 요리를 한 번 볼 티니."
    jump chapter1_1_2

label chapter1_1_2:
    scene c1-2 with dissolve   #리스의 집-주방

    ch_na "이번에는 주방 쪽만 움직이니 청소할 때보단 덜 걷겠네."
    "근데 어쩌면 청소보다 더 힘들 수도 있겠어. 요리란 게 손맛을 크게 타는 일이잖아."
    r "냉장고 안에 필요한 재료는 다 있을 기니, 맛난 걸로 알아서 만들으라."
    ch_na "-덜컥."
    "3개로 이루어진 냉장고 문을 모두 열었더니 각양각색의 재료들이 다 있네. "
    "한쪽은 고기, 다른 한쪽은 해산물과 채소가 있고... "
    "어우, 나머지 한쪽은 온갖 술로 가득 채워져 있네. 술꾼이구만."
    "그래도 일단 식재료가 다 좋아 보여가지고 괜찮네. 웬만한 음식들은 다 만들 수 있을 것 같아."
    "허나 내가 평소에 요리를 자주 하지는 않는 게 문제인걸."
    "기사단에서 취사를 담당했을 때마다 요리해 본 경험만 있었지, 그 외에는 별 기억나는 것도 없고..."
    "그 경험이라도 한 번 살려보도록 하자고. 보통 귀족들은 뭘 좋아할까."

    #선택지
    menu:
        "선택지1 : 레스토랑 풍의 스테이크":  
            jump chapter1_1_2_a

        "선택지2 : 매운 향이 가득한 볶음밥":  
            jump chapter1_1_2_b

label chapter1_1_2_a: # 스테이크
    ch_na "일단 가장 생각나는 건 케이크 종류의 디저트 아님 스테이크인데..."
    "내가 베이킹을 해본 적은 거의 없었지. 어렸을 때 체험식으로 해본 걸 빼면."
    "그럼 스테이크로 가자. 요리 잡지에서 봤던 레시피가 있었으니, 그 기억을 되살리면 될 거야."
    "우선 두툼해 보이는 고기부터 밑간하는 걸로 시작해볼까. "
    "저 작은 병 안에 든 가루가 시즈닝할 때 쓰는 거겠지. 그걸 고루 뿌려주고..."
    "간이 베이는 동안 채소를 손질하면, 모든 준비가 끝나는 거다. 이제 팬을 꺼내 굽는 일만 남았네."
    "-스윽."
    "어우, 이 팬 생각보다 묵직하네. 그쪽 세계에 썼던 건 이보다 훨씬 가벼웠는데."
    "어쨌든 고기를 구워보자고. 이 V자형으로 생긴 게 아마 고기를 뒤집는 거겠지."
    "팬에 기름을 넉넉하게 둘러 뜨겁게 달궈준 다음에 연기가 올라오면은..."
    "-촤르르르~" #[고기 굽는 효과음]
    "크으! 이 소리 참 간만에 들어본다. 팍 터지면서도 자글자글거리는 순간을 누가 안 좋아하겠어?"
    "아, 그러고 보니 굽기 정도도 생각해야지."
    "한 미디움 정도면 되려나. 그게 가장 무난할 거야."
    "이제 뒤집어볼까. 어떻게 구워졌나..."
    m "...으앗!"
    ch_na "세, 세상에. 표면이 모두 검게 타버렸잖아!"
    "분명 이때 뒤집는 게 맞았을 텐데. 내가 시기를 잘못 계산했나? 아님 팬과 기름의 특성이 내가 살던 데하고 달라서 그런가?"
    "아이 씨, 망했다! 이걸 어떻게 꼼수라도 부릴 수 있나."
    "이, 일단 다 굽고 나서 검은 부분만 손질하든가 하자고... 그 외에는 별문제가 없겠지?"

    "- 잠시 후 -" #[화면이 꺼졌다가 다시 켜지는 연출]
    scene c1-2 with eyeclose

    m "완성됐습니다, 드셔 보세요."
    r "오오, 스테이크라... 눈치 하나는 좋네."
    ch_na "한땀한땀 정성들여 플레이팅한 스테이크를 리스가 넋 놓으며 들여다보고 있었다."
    "플레이팅은 깔끔하게 윗쪽에는 채소를, 아래쪽에는 고기를 두어 반달 모양처럼 놓았지. "
    "일단 첫인상은 좋구만. 잠깐 한숨이 놓이네."
    r "비주얼은 괜찮아 보이는구마. 그럼 한 번 먹어볼까나..."
    ch_na "-슥슥."
    "리스가 나이프로 스테이크를 썰어 맛볼 준비를 하기 시작했다."
    "고기 단면은... 어라, 속이 완전히 익어버렸는데? 내가 생각한 미디움은 아닌 걸..."
    r "아음..."
    ch_na "한 입 크기로 잘 썰어가지고 입 안에 넣었네."
    "그래도 밑간은 적당히 했으니 적어도 고기 맛은 보장되어 있겠지." 
    r "으응...?"
    ch_na "아 이런,  표정을 살짝 찌푸렸는데, 고기에서도 문제가 있나?"
    r "아우, 너무 질기네... 고무를 씹는 느낌인데."
    ch_na "역시 고기가 탔을 때가 불안하다 싶더니, 이렇게 정곡을 찌르네."
    "근데 솔직히 내가 100%% 잘못한 건 아니라고 생각하는데, 일단 이쪽 기름과 내가 살던 곳의 물건이 똑같겠어?"
    r "간도 참 씨게도 짜게 혔구마. 물 좀 실컷 마셔야 쓰것다카라."
    ch_na "시즈닝까지? 에흐, 망했구만. 제일 중요한 고기 맛을 망쳐버렸어. "
    "이거 평가가 애매하겠네. 접시 세팅은 제법 잘 한 것 같은데..."
    r "아무래도 요리 경험은 별로 읎는 것 같구마. 요걸 읽으면서 배워야 쓰것다."
    ch_na "리스가 고개를 저으며 건네준 책은 요리책이었다. "
    "'초보자도 레스토랑 음식을 만드는 비법!'이라... 그래, 나 아직 초짜다."
    "갈고 닦아야지 뭐, 그럼 어쩌겠어. 또 이렇게 만들면 불만이 계속 샐 텐데."
    jump chapter1_1_3  #[선택지1 구문 종료]


label chapter1_1_2_b: # 볶음밥
    ch_na "어쩌면 이런 간단히 만들 수 있는 음식이 오히려 좋은 반응을 받을 수도 있어."
    "귀족이 항상 금가루 들어간 음식만 먹지는 않잖아. 축제 때 길거리에서 꼬치 같은 걸 사 먹는 귀족들도 봤는데."
    "그래, 이게 그나마 가장 자신있어하는 음식이니 그걸로 가보자."
    "고기와 야채를 잘게 다지고, 밥과 함께 프라이팬에 넣은 뒤..."
    "-촤르르~" #[볶는 효과음]
    "스파이시한 소스를 넣고 불맛이 나도록 센 불로 빠르게 볶아주었다."
    "볶으면서 나는 향이 굉장히 좋네. 살짝 맛을 보니 간도 잘 배여 있고."
    "맵찔이가 아닌 이상 이걸 리스가 안 좋아할 수 없겠지."
    "- 잠시 후 -" 
    #[화면이 꺼졌다가 다시 켜지는 연출]
    scene c1-2 with eyeclose

    m "완성됐습니다, 드셔 보세요."
    r "으음, 볶음밥이가? 기래, 좋은 향이 도는구마."
    ch_na "리스가 볶음밥이 담겨있는 접시를 보며 고개를 끄덕였다."
    "제법 평범한 음식이라 살짝 걱정은 됐었는데, 예상외로 괜찮은 반응이라 다행이네."
    r "자, 한 번 먹어볼까나... "
    ch_na "-덥석."
    "리스가 숟가락으로 볶음밥을s 퍼 한 입 덥석 물었다."
    "볶음밥을 천천히 음미하며 삼킨 뒤에 어떤 소감을 말할지..."
    r "오호라! 맛이 아주 좋구마. 진하게 매운 향과 감칠맛이 감돈다카라!"
    ch_na "리스가 내가 만든 볶음밥에 대해 온갖 칭찬을 아끼지 않았다."
    "후우... 좋아해 줘서 고맙네. 내가 만들어준 음식을 먹고 맛있다고 하면 평가는 뻔하지."
    r "이 정도면 합격점을 줘도 되겄구마. 잘헛다. 음식 솜씨가 괜찮구마."
    m "감사합니다."
    ch_na "평가 후 리스는 계속 감탄을 자아내며 볶음밥을 계속 흡입하였다."
    "밥 한 톨도 남기지 않고 먹는 걸 보면 이런 걸 좋아하는 모양이네. 원래 저런 음식을 자주 즐겨 먹나?"
    r "근데 니, 다른 요리도 할 줄 아나?"
    m "다른 음식도 어느 정도 만들 줄 알지만..."
    m "고급 식당에서 나올 법한 비싼 음식들은 만들어보질 못했습니다."
    r "그렇나... 기럼 요게 도움이 될 기다."
    ch_na "리스가 내게 한 권의 책을 건네주었는데, 요리책이네. 표지에 음식들로 가득 차 있으니까."
    "'초보자도 레스토랑 음식을 만드는 비법!'이라... 그래, 시간날 때 비법을 확실히 전수받아 보자고."
    jump chapter1_1_3 #[선택지2 구문 종료]

label chapter1_1_3:
    scene c1-1 with dissolve   #리스의 집

    m "하아... "
    r "테스트는 모두 끝났다카라. 수고혔다."
    ch_na "빨래, 정원 관리 등을 더 거치고 난 다음에야 모든 테스트를 끝마칠 수가 있었다."
    "테스트라는 게 이렇게 길었나. 기사단의 입단 시험도 이 정도까지는 아니었는데 말이다."

    #[청소 - 선택지1, 요리 - 선택지1 선택 시의 구문]
    #r "...뭐, 말 안 혀도 알긋제?"
    #m ...네.
    #r "집사라 부르기에도 민망할 정도였다카라. 발전하는 데 시간이 꽤나 걸리겄어."
    #"전체적으로 나사가 빠진 부분이 많기는 했어. 아직 여기에 온 지 얼마 안 돼 마음이 복잡했던 부분도 있었고..."
    #"이 악물고 발전하도록 노력해야지. 여기가 밑바닥이라 생각하고 갈고닦아보자."
    #r "정신 차리고 일로 오도록."

    #[청소 - 선택지2, 요리 - 선택지1 선택 시의 구문]
    #혹은 [청소 - 선택지1, 요리 - 선택지2 선택 시의 구문]
    r "대략 요약하자믄, 괜찮은 부분도 있고 마음에 안 드는 부분도 있어 아주 좋은 점수를 주기는 힘들 것 같구마. 뭐가 원인인지는 잘 알긋제?"
    m "그런 부분은 반드시 고쳐보도록 노력하겠습니다.  "
    ch_na "중간마다 리스의 지적을 피해 갈 순 없었지만, 그럭저럭 잘 진행된 것 같았다. "
    "정말이지, 이 세계에 오면서 처음으로 숨 막히는 순간들이었어."
    r "기래, 저런 말이 나와야 믿음직스럽지. 일로 오라."

    #[청소 - 선택지2, 요리 - 선택지2 선택 시의 구문]
    #r "증말로 내가 딱 원했던 부류였다카라. 매사에 꼼꼼하고 집중하는 모습 하나는 마음에 든다. 성격만 살짝 고친다면..."
    #m "아아, 그건 제가..."
    #r "내도 안다. 아직 여그로 온 지 얼마 안 됐으니 예민할 수밖에 읎겄제."
    #"내가 평소에는 성격이 그리 거칠지 않은 편이다. 부하들을 훈련이나 전투 등의 상황에서 막 함부로 대하지 않았고."
    #"이 세계에서 워낙 황당한 일들을 많이 겪다 보니 잠깐 정신이 안드로메다로 간 거지. "
    #"아무리 긍정적인 사람이라도 이런 일들을 한꺼번에 겪으면 감당하기가 정말 힘들 거야."
    #"그걸 이해해주는 걸 보니까 살짝 마음의 문이 열리네, 안도감이 들어."
    #r "자, 일로 오라, 믿음직한 집사여. 기막힌 걸 보여줄 티니."
    #[선택지 구문 종료]


label chapter1_1_4:
    scene c1-3 with dissolve   #매시안의 침실

    ch_na "-끼익." #[문 여는 효과음]
    r "실컷 구경해보라. 여그가 앞으로 집사가 지낼 곳이니."
    m "우와..."
    ch_na "리스가 문을 열어 나한테 보여준 건 입이 쩍 벌어질 정도로 널찍한 공간을 가진 방이었다."
    "거대하고 푹신해 보이는 침대도, 경치가 탁 트인 창문도 있다니. "
    "화장실도 들여다봤는데, 호텔 목욕탕 뺨찔 정도로 깔끔했다."
    "넓은 욕조가 있어 샤워하기에도 정말 편해 보여. 미쳤는데?"
    m "여, 여기서 지내면 됩니까? 정말로요?"
    ch_na "이 정도면 기사단에서 지냈던 숙소보다 훨씬 좋잖아?"
    "병사 시절에 동기들이랑 좁은 곳에서 다 같이 지냈던 것 생각하면, 이런 공간은 내게 큰 축복이나 다름없지."
    r "흐흐, 놀랄 먼 하네. 이런 방은 귀족이나 대기업 회장 같은 사람들만이 지내는 곳이니."
    m "딱 봐도 그래 보이더라고요."
    ch_na "역시 귀족은 귀족이구나. 방 하나하나가 오피스텔 한 채 갖다 놓은 것 같다니까." 
    r "어이, 집사."
    m "네."
    r "인자 내한테 말 놔도 된다. 물어볼 게 있음 편하게 대답하고."
    m "어, 정말로요?"
    r "기래, 나이 차도 별 안 나고 어느 정도 같이 있을 사이인디, 존칭은 어색하다고 느껴지지 않나?"
    ch_na "이 시간 이후부터 반말을 해도 상관없다고 한다라."
    "눈치가 빠른 건지는 아직 모르겠지만, 어쨌든 답답한 속이 뻥 뚫리는 기분이었다."
    r "뭐, 반말로 해보고 싶은 말이 있음 해보라. 함 들어는 볼게."
    m "흐흠..."
    ch_na "이 근질거리는 입속에서 뭘 내뱉을지 고민이네. 뭐가 좋을까..."

    #선택지
    menu:
        "선택지1 : 잘 자":  
            jump chapter1_1_4_a

        "선택지2 : 쓰레기 같은 X":  
            jump chapter1_1_4_b

        "선택지3 : 고마워":  
            jump chapter1_1_4_c

label chapter1_1_4_a: # 잘 자 선택

    m "피곤할 텐데 얼른 자. 고생 많았어."
    r "...기래. 니도 피곤할 틴디 푹 쉬라."

    "깜깜해진 지 한참 됐으니 저런 말을 건네주는 게 맞는 일이겠지. 눈이 침침해 보이는 것 같기도 하니."
    jump chapter1_1_4_ #[선택지1 구문 종료]
 
label chapter1_1_4_b: # 쓰레기 같은 X 선택

    m "이 납치범 녀석! 감히 날 여기에 가두려 하다니, 내가 가만히 있을 줄 알아?!"
    r "..."
    ch_na "후아, 속이 다 시원하네. 이런 말을 꼭 해보고 싶었거든."
    "그동안 날 계속 갈궜겠다? 그럼 이것도 맞받아 쳐보시지 그래? "
    "아이고, 화났어요? 화나면 뭐 어쩔 건데? 열불내는 거 말고 네가 뭘 할 수 있는..."
    r "이 빌어먹을 놈이 그냥...!"
    "-빠악! 빠악!" #[화면이 흔들리는 연출 x2]
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "으악! 아야야! 아야야야!"
    ch_na "리스의 무수하고 강력한 꿀밤 세례가 내 머리를 강타했다."
    "한 두대 정도만 때릴 거라 생각했는데. 어, 어지러워..."
    r "이 자슥이 반말을 허용했더니 맞고 싶어 안달이 났구만...!"
    m "그래도 날 납치해서 여기다 끌어들인 건 맞잖아. 내 말이 틀렸어?"
    r "오호라, 이런 식으로 기강을 잡을라고?"
    "-꽈악."
    ch_na "리스의 눈가에 불길이 활활 타오르며 전보다 더 센 꿀밤을 먹일 준비를 했다."
    "저 정도면 내 머리가 버틸 수 없겠는데? 어, 얼른 태세 전환을..."
    m "아, 알았어! 미안해! 미안하니까 그 주먹은 일단..."
    "-빠아아악!" 
    #[화면이 격하게 흔들리는 연출]
    with Shake((0, 0, 0, 0), 0.3, dist=40)
    m "끄에에에에에엑!!"
    ch_na "..."
    "...멱이 따이는 기분이네. 으으..."
    "난 혹이 난 머리를 쓰다듬으며 고통이 빨리 해소되길 빌었다."
    "내가 너무 리스를 얕본 것 같아. 앞으로는 좀... 조심해야겠네. "
    jump chapter1_1_4_ #[선택지2 구문 종료]


label chapter1_1_4_c: # 고마워 선택

    m "그럼 감사인사를 할게. 살 길을 트이게 해준 건 고맙다고 생각하고 있어."
    r "어... "
    ch_na "갑작스런 감사인사에 리스가 어색한 표정을 지으며 얼굴을 살짝 붉혔다."
    "여기까지 오며 뭐 찔리는 거라도 있어서 그런 건가. "
    "하긴, 독설을 밥 먹듯이 한 게 가장 생각났을지도 모르겠지."
    r "기렇게 생각한 이유라도 있나?"
    m "그렇지 않았음 계속 떠돌이짓을 했겠지. 낙오된 외국인이나 다름없잖아, 내가."
    r "으, 으흠... 맞는 말이긴 혀지."
    ch_na "잡혀있는 신세일지라도, 일단 이 세계에서 정상적으로 지낼 수 있게 해줬다는 건 사실이니까."
    jump chapter1_1_4_ #[선택지3 구문 종료]

label chapter1_1_4_:
    r "자, 내는 가보겠다카라. 내일 보자고."
    ch_na "-탁."
    "드디어 다사다난했던 하루가 막을 내렸네."
    "갑자기 한국이란 땅에 오지 않나, 여기로 끌려오지 않나, 여고생 뻘 되는 애의 집사가 되지 않나..."
    "오늘 경험한 것들은 다시 생각해도 이해할 수가 없는 일이었다."
    "내게 지금 무슨 일이 일어난 건지 모르겠어. 이걸 좋아해야 할지, 싫어해야 할지."
    "근데 왜, 피로가 전혀 안 느껴지지?  "
    "이제 밤도 깊어가니 반쯤 눈이 감겨야 정상인데 말이야."
    "고된 하루를 보냈는데도 내 몸에서는 조금의 피로도 느껴지지 않았다. 오늘 컨디션이 좋아서 그런가?"
    "일단 목욕부터 해야겠다. 뜨거운 욕조에 담가 밝은 미래를 향한 망상이나 취해봐야지."
    "-스륵."
    "난 목욕을 하기 위해 차례차례 옷을 벗기 시작했다."
    "먼저 손에 낀 장갑부터 떼어내고..."
    m "...으엣!"
    ch_na "장갑을 떼는 순간, 난 내 손을 보며 화들짝 놀랐다."
    "보통 사람들의 피부는 살구색 아니야? 어떻게 내 손이 하얄 수가 있지?"
    "그럴 리가 없어. 손에 뭐가 칠해진 게 분명할 거야. 화장실로 가서 손을 닦으면 되겠지. "
    m "에에에엣?! 이, 이게 뭐야?! "
    ch_na "화장실에 놓인 거울에서 얼굴을 보자마자, 난 또 경악할 수밖에 없었다."
    "얼굴 피부도 손과 마찬가지로 하얀색으로 뒤덮였으니까."
    "갑자기 왜 이렇게 변할 걸까? 이 세계로 넘어온 영향인 건가?"
    "가만, 그럼 내 온몸도... 그렇게 덮여 있지는..."
    m "..."
    ch_na "예상은 정확했다. 옷을 다 벗은 후에 봤을 때도, 머리부터 발끝까지 모두 하얀색으로 되어 있어."
    "맙소사, 온몸을 보니 내가 지금 사람이 아닌 외계인인 것 같잖아."
    "그냥 전부 다 페인트로 칠한 거라 믿고 싶어. 그래, 목욕을 해보자!"
    "-쏴아아아." #[욕조에 물을 붓는 효과음]
    "뜨거운 물을 받은 욕조에서 몸을 담그고, 시간이 됐다 싶으면 때를 벗긴 다음..."
    "샴푸랑 바디워시를 이용해 온몸을 닦아서 하얀색 피부를 원래의 살구색 피부로 바꾸려 애를 썼다."
    "좋아, 이렇게 하면... 이렇게 하... 면..."
    m "안 돼... 계속 이러면 안 되는데!"
    ch_na "괜시리 기대했나. 불행하게도 내 하얀색 피부는 목욕하는 거로도 바뀌지 않았다. 괜한 헛수고일 뿐이었지."
    "하... 이 모습으로 계속 살아가야 한다고? 갑자기 눈앞이 막막한데."
    "-털썩."
    "피부에 너무 충격을 받은 탓일까. "
    "난 그것 때문에 한동안 침대에 주저앉아버렸다."
    "도대체 내가 왜 이리됐을까. 내 피부가 약한 것도 아닌데."
    "그 생각에 나는 도저히 잠이 오질 못했다..."
    "아니, 잠이 오지 못했기보다는 잠이 아예 안 왔다."
    "이것도 무슨 이유인지는 모르겠지만, 피곤하다는 생각이 눈곱만큼도 들지 않았다. "
    "진짜 내 몸 상태가 어떤지를 모르겠네. 이상현상이 생긴 게 분명한데, 그 이유를 알 수가 없어."
    "진짜 나한테 뭔 일이 일어난 거냐... 내 인생 왜 이렇게 꼬이는 거냐고!"


#[챕터 1-2]
label chapter1_2:
    scene c2-1 with dissolve   #매시안의 침실
    
    ch_na "-짹짹."

    "잠시 패닉에 빠진 지 얼마나 됐다고 벌써 새가 우는 시간이 됐냐."
    "지금이 몇 시이길래... 앗, 6시 30분인가."
    "한국에서도 이 시간쯤 되면 이른 아침이라 부를 만한 때겠지. "
    "리스는 언제쯤 일어나려나. 그러고 보니 몇 시에 일어나는지를 못 물어봤네."
    "아직 스케줄도 못 짰고 내가 집사란 직책도 잘 모르는 상황이긴 하지만..."
    "그래, 일단 나가보자. 부딪혀보면 알겠지."
    "보통 이때쯤이면 집사가 활동을 시작하는 순간이기도 할 거고."

label chapter1_2_2:
    scene c2-2 with dissolve   #리스의 집(거실)
    ch_na "어우, 햇빛이 거실 창문으로 확 비치네. 여긴 일광욕하기에도 나쁘지 않겠는데?"
    "근데 주위에 리스는 안 보이는구만. 미동도 안 느껴지는 걸 보니 아직 자기 방에서 자고 있겠지."
    "그렇다면 슬슬..."

    #선택지
    menu:
        "선택지1 : 리스를 깨울까.":  
            jump chapter1_2_2_a

        "선택지2 : 아침 식사를 준비할까.": 
            ch_na "좋아, 아침밥을 안 먹으면 힘이 나질 않을테니." 
            ch_na "간단하게라도 한 번 차려보자. 요리책에서 눈여겨봤던 게 있기도 하니까." 
            jump chapter1_2_2_b_

label chapter1_2_2_a: #리스를 깨울까
    ch_na "뱀파이어는 평소에 일찍 일어날 것 같은데. 일단 햇빛을 받는 걸 별로 안 좋아하니까."
    "그렇게 생각하면 지금은 늦잠을 자고 있다는 뜻이겠지."
    "물론 100%% 정답이라고 확신할 수는 없어. 아직 서로에 대해서 잘 모르니까."
    "그럴 때 억지로라도 깨우는 시도라도 하면서 알아가는 것도 의외로 괜찮은 수단이거든. "
    "뭐든 간에 관계가 발전하기 위한 첫걸음에는 이런 무리수를 둘 정도의 용기가 필요하니까."
    "리스의 침실이 바로 윗층에 있었지. 어제 청소했을 때 들어가봤으니."
    "-탓탓."
    "그래, 문 주위가 꽃과 리본으로 장식된 게 딱 여자가 지내는 방이라고 새겨져 있네."
    "그럼 어디 한 번 노크를..."
    "-똑똑."
    m "주인, 일어날 시간이야."
    "-똑똑똑."

    m "주인?"

    "아무리 노크해도 대답이 없네. 얼마나 푹 자고 있길래..."
    "아직 꿈나라에서 깨어나지 못한 건가."
    "-따르릉! 따르르릉!"
    "어우, 깜짝이야. 한 번 더 노크해보려 시도하던 참이었는데... 미리 알람을 맞추고 잤나 보네." 

    r "아으..."

    "알람이 울린 지 얼마 안 될 쯤에, 안에서 리스가 기지개를 피며 하품을 내쉬는 듯하였다."
    "이후 슬리퍼 소리와 함께 문 쪽으로 가까이 다가오더니..."
    "-드르륵."

    r "으음... 웬 노크소리가 들리는가 혔더니..."
    r "내 깨우려고 왔나?"
    m "어, 어..."

    "눈을 비비며 드러낸 리스의 모습은 어제와는 제법 상반된 분위기였다."
    "고스로리 드레스에서 파자마로 갈아입으니 고고한 귀족에서 앳된 소녀 같은 느낌으로 변했다고 해야 하나."
    "근데 머리는 언제 그리 빨리 묶었대. "

    r "그... 깨우는 거 땜에 여그로 안 와도 된다카라. 알람이 있으니께."
    m "알았어. 기억해둘게."
    r "근디 니도 알람 맞추고 잤나? "
    m "아아, 난 잠이 안 와갖고."
    r "응? 평소에 잠을 설치는 편이가?"
    m "아니, 설쳤다기보다는 자고 싶다는 생각이 전혀 안 들었거든."
    r "에에~ 기런 사람이 어디 있다고..."

    "나도 믿겨지지가 않아. 불침번을 수없이 섰어도 불면증 같은 증상은 없다고 건강검진 때 항상 들었었는데."
    "난 원래 제시간에 잠을 꼬박꼬박 자는 타입이었으니까. 그러니 더욱 아리송할 수밖에."

    r "암튼, 나가 일어나기 전엔 아침부터 만들어 놓으라. 기래야 나가 좀 편해지니께."
    m "근데 보통 아침엔 뭘 주로 먹어?"
    r "갑자기 그건 와... 아, 기러고 보니 깜빡한 게 있었구마."
    r "따라오라. 뭔가 보여줄 게 있으니."
    "갑자기 보여줄 게 있다는 건..."
    "설마, 서프라이즈 선물인가? 어제 날 막 다룬 거에 대한 사과 겸 해 가지고?"
    jump chapter1_2_2_a_
        
label chapter1_2_2_a_:
    scene c1-2 with dissolve   #주방
    
    r "오늘 나가 어떠케 아침을 준비하는 지 보라. 다음 날은 네 몫이다카라."
    "그럼 그렇지. 앳된 소녀스런 분위기는 겉멋이었구만..." 
    "그냥 큰 방에서 지내는 걸로 쌤치자 생각하는 게 좋겠다. 그것만 해도 감지덕지하기에는 충분하고도 남잖아."
    r "자, 요건 토스트란 빵이고 저건 토스트기인기라. "
    r "토스트기에다 이 빵을 넣으믄 바삭혀게 구워지제."
    m "팬에다 안 구워도 되는 거야?"
    r "그러니 요 기계를 들인 거지. 편리하니께."
    "딱 보니까 기계의 구멍이 토스트만 딱 들어갖게끔 맞춰져 있네." 
    "말 그대로 토스트를 구울 때 쓰는 놈이구만."
    "-철컥."
    "리스가 토스트기 안에 빵을 넣고 스위치를 내리자, 째깍거리는 소리가 자그마시 들리기 시작했다."
    r "그리 오래 걸리진 않을 기다. 타이머도 토스트기로 맞춰놨고."
    "오오, 손을 가까이 대보니 열이 굉장한데. 노릇노릇한 냄새도 나는 것 같아."
    "열기를 보니 금방 완성될 것 같은데. 기대되네, 어떻게 나올지."
    "-띵!"
    r "꺼내보라. 어떻게 구워졌는지."
    m "우오오..."
    "토스트를 안에서 꺼내자, 새하얗던 토스트의 속살이 갈색으로 짙게 물들었다."
    "살살 긁어보니 되게 바삭할 것 같은 느낌도 나고 그래. 것보다 탄자국이 없다는 게 신기할 따름이네."
    r "함 맛 봐 보라. 니한테도 맞을 걸."
    "-와삭."
    "우앗! 한 입 물자마자 퍼지는 이 쫀득하면서도 바삭바삭한 식감이라...!"
    "나도 아침에 토스트로 해결할까? 먹기에도 간편하지, 맛도 있잖아."
    r "괜찮제?"
    m "응, 되게 맛있다 이거."
    "-덜컥."
    "둘이서 같이 토스트를 해치운 뒤, 리스가 냉장고 문을 열어 아침 만드는 거에 관한 얘기를 꺼냈다."
    r "이곳 냉동실에서 항상 토스트를 보관하니께. 앞으로 토스트를 사믄 여그다가 넣으믄 되고..."
    r "옆에 있는 냉장실에는 아침 재료가 든 층이 있다카라. 거기 있는 재료를 꺼내가 쓰믄 되는 기라."
    m "아침에는 이렇게 있는 걸로만 먹어?"
    r "보통 그렇게 먹제. 와, 집사가 하는 아침은 좀 다른가?"
    m "매번 반복해서 먹는 것 같아서."
    r "하, 기런 거로 걱정하기는..."
    "아침에 별 신경 안 쓰는 걸 보면 아침에 저런 걸로 계속 먹는 것이 지겹지 않나 보네."
    "하긴, 아침엔 보통 일정이 있음 빨리 만들고 빨리 먹고 가는 게 낫긴 하지."
    r "원한다믄 굳이 이런 매뉴얼대로 하지 않아도 된다. 단, 맛은 절대 실망시키지 말그라."
    m "알겠어요, 입맛 까다로운 주인 나으리."
    "-빠악!" 
    #[흔들리는 연출]
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "끄엑!!"
    r "나가 방금 맛만 실망시키지 말라 기랬지 은제 입맛이 까다롭다 혔냐?"
    r "평타 정도만 치믄 나가 뭐라 안 혀니 억지로 부담 갖지마라.  것 참, 웬 헛소리를 하는가 혔더니..."
    "그게 입맛이 까다로운 거잖아요, 이 양반아! 평타 맞추기도 얼마나 어려운 일인데!"
    "어우, 그 와중에 아침인데도 힘이 되게 팔팔하네. 꿀밤 맛이 기가 막혀."
    jump chapter1_2_3

label chapter1_2_2_b_:
    scene c1-2 with dissolve   #주방
    "-덜그럭."
    "그게 어디 있었지... 오, 여기 있다!"
    "라벨을 읽어보니 이게 한국에서 주로 먹는 가공육 중에 하나일 거야, 이름은 '르네피언 소시지'라고 적혀있고."
    "고기를 갈아 길쭉한 원통 모양처럼 만든 식품이라, 특이하네. "
    "일단 육류를 이용해 만드니까 어느 정도의 맛은 보장되어 있을 테니 한 번 써봐야지."
    "그 다음은 주식으로 삼을 걸 구해야 하는데..."
    "어, 잠깐만... 여기 라벨에 빵이라고 쓰여있는 게 있잖아? "
    "빵은 에르온에서 자주 본 음식이라 익숙하긴 해. 에르온에도 다양한 바리에이션이 있고."
    "저걸 보니까 표면은 바삭하고 안은 부드러워 보이는 게 어떤 맛일지 궁금하게 만드는구만."
    "이름은 ‘곡물식빵’, 부제에는 아침 해결사라, 확실한 주식이네. 하핫..."
    "어쨌든 이 정도면 충분하겠어. 제법 괜찮은 접시가 나올 거란 예감이 들어."
    #[화면이 암전됐다가 다시 나오는 연출]
    define eyeclose = Fade(0.5, 0, 1, color="#000000")
    "-탁."
    "역시 재료랑 조리법이 간단해서 그런가, 금방 끝냈네."
    "그냥 굽기만 했는데도 먹음직스러운 비주얼이 나온다는 게 사실이었구나. 요리책으로만 봤을 땐 약간 미신이라 여겼는데."
    r "으으으음..."
    "오, 시기를 잘 맞춘 것 같네. 보통 이때쯤에 일어나는구나, 리스가."
    "잠옷 입은 걸 보면 보통 아침 먹고 환복하나 보지."
    m "일어났어?"
    r "기래... 나가 요때 일어나는 걸 어찌 알았는지는 모르겠다만..." 
    m "늦잠 부릴 것 같지는 않아 보였거든. 혈기가 넘치는 것도 그렇고."
    r "...니 뭐 독심술이라도 부맀나?"
    "그냥 한 번 해본 소리야. 굳이 따지자면 사람을 많이 만난 경험이라고나 할까."
    "기사단에서도 전투에서도 온갖 다양한 유형의 사람을 봤으니..."
    r "기럼, 아침 솜씨를 함 짚어보도록 할까."
    "-텁."
    "리스가 접시에서 먼저 택한 건 붉게 익은 소시지였다."
    "한 입 덥석 베어물었을 때, 펑 터지는 소리와 쫀득쫀득한 식감이 그녀의 입안을 황홀하게 감싸는 것 같았다."
    r "호오, 육즙이 풍부하구마! 잘 구웠는데?"
    "좋아, 소시지는 호평이다. 그럼 이어서 빵 쪽은 어떨지..."
    r "으으음... 으흠..."
    "빵을 씹을 때도 입가의 미소는 전혀 사그러들지 않고 있네."
    "이 정도면 아침 식사 가지고 불평 들을 일은 없을 것 같은데?"
    r "제법 괜찮은 차림이었다카라, 잘 혔네!"
    "아침 식사에 관한 결과는 호평으로 막을 내렸다."
    "근데 사실 내가 잘했다고 하기에는 뭐한 게, 소시지와 빵의 맛은 사전에 어느 정도 보장된 덕분인지라."
    "그런 점이 이 접시의 절반 이상을 차지했다고 봐도 무방하지, 흐흠..."
    "다음에는 테크닉을 감미해서 만들어보고 싶네. 그럼 더 좋아해 줄지도."
    jump chapter1_2_3

label chapter1_2_3:
    scene c1-2 with dissolve   #주방
    #[화면이 암전됐다가 다시 나오는 연출]
    define eyeclose = Fade(0.5, 0, 1, color="#000000")
    "-챠륵 챠륵..."
    "식사를 마쳤을 땐 설거지를 하는 건 기본이지. "
    "어제는 정신없어서 깜빡하고 못했기에, 오늘이 여기서 하는 첫 설거지다."
    "방식이 전에 살던 곳하고 다를까 불안하긴 했지만, 생각보다 비슷했기에 별 탈은 없었어. "
    "취사병 시절에 했던 걸 바탕으로 요령을 떠올려내 수월하게 끝냈지. "
    m "후우!"
    "삐까뻔쩍한 식기들을 보니 금세 보람이 차는구만. 찌꺼기 한 풀도 남아있지를 않네."
    r "다 마쳤나?"
    m "저거 봐, 깔끔하잖아?"
    "분명히 저걸 가지고 퇴짜맞을 이유는 없겠지. 내가 얼마나 꼼꼼하게 했는데."
    r "기래 기래, 대충 봐도 알긋다."
    "에헤이! 그동안 했던 것 중에서 제일 열심히 한 건데, 그냥 눈흘림으로 끝내네."
    "괜히 고생해서... 아니다, 자화자찬으로 만족하면 되지."
    r "집사."
    m "뭐 물어볼 거라도?"
    r "그런 게 아이고, 내 일하는 데에 따라올 마음 있나?"
    "일하는 곳? 여기가 일하는 데 아닌가?"
    "귀족들은 여기서 업무 보고 식사 하고 잠 자고 하루를 대부분 여기서 보낼 텐데.."
    "아님 내가 너무 편견에 사로잡혀 있는 걸 지도... "
    "그러고 보니 귀족 출신 가수도 존재한 사례가 에르온에서도 있었지."
    "가창력은 그럭저럭인데, 돈이 많아서 그런지 성형에 행사에 이것저것 팍팍 쏟아붓더라고."
    "리스도 그런 부류에서 활동하나."
    r "니 마음대로 혀라. 집에서 나뒹굴고 싶음 기냥 여그에 있고."

    #선택지
    menu:
        "선택지1 : 한 번 따라가볼까.":  
            jump chapter1_2_3_a

        "선택지2 : 나 홀로 집에...": 
            jump chapter1_2_3_b





return