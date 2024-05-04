
label s2:
    scene p2 with flash  # 어느 산속
    play music "audio/02Mountains.ogg"
    
    ch_na "눈을 떠보니, 새들의 울음소리와 동시에 태양이 내리쬐는 산속이었다."
    "이곳이 천국인가. 내가 살았던 세계와 비슷해 보이는데."
    "아니면 천국으로 향하는 입구일지도 모르겠지. 새로운 인생도 익숙한 장소를 시작으로 서서히 미련을 버리면서 가는 거잖아." 

    #잠시 대기하는 연출 및 효과음('cloth wear.ogg') 추가  - 수정
    scene p2 with collect
    play sound "audio/sfx/cloth wear.ogg"
    "어라? 몸을 살짝 움직였더니..."
    "아, 몸에 뭔가 걸쳤구나." 
    "긴 검은 셔츠에 남색 바지, 회색 장갑, 그리고 모델이 입을 것 같은 하얀 코트까지 있네."
    "전체적으로 꽉 끼지도 않고 헐렁하지도 않고, 적당해. 죽기 전에 입었던 옷과는 확실히 달라."
    "내가 갑자기 왜 이걸 입었는지 의아하긴 하지만... 그래도 알몸으로 있지 않은 게 어디냐."
    "그건 그렇고, 일단 여기가 뭐 하는 곳인지는 알아봐야겠지. 어디 구경할 만할 데가 있나."


label s3:

    #dissolve : 장면을 자연스럽게 전환할 때 사용
    # 걷는 효과음 추가('walk.ogg') 

    scene p3 with dissolve # 부산 시장가
    play sound "audio/sfx/walk.ogg"
    ch_na "-터벅... 터벅..."
    "산 속에서 빠져나오니, 시장처럼 보이는 골목이 나왔다."
    "상점들이 빼곡하게 자리 잡고 있었고, 사람들이 와글대며 골목을 거닐고 있는 걸 보면 인기가 많은 곳인가 보다."
    "이곳저곳에서 물건을 사고파는 상황들로 가득하니 여기가 천국에서 잘나가는 시장 중 하나겠지."
    "그건 그렇고, 이곳에 왔으면 일단 뭐부터 해야 하지?"
    "아, 그래. 여기도 입국 허가 절차 같은 게 있을 거야."
    "일단 공항으로 가야겠다. 정식으로 입국 신고를 해야 천국 사람이라고 인정받을 수 있을테니까."
    "저기 생선을 파시는 아줌마한테 한 번 물어봐야지. 여기에 대해서 잘 아실 테니 말이야."

    play sound "audio/sfx/select button.ogg"

    # 선택 버튼 효과음 추가('select button.ogg') 
    #선택지
    menu:
        "선택지 1 : OOOOOOOO?":  
            # 클릭 버튼 효과음 추가('click button.ogg')
            # 텍스트 글리치 효과 추가({glitch=50.0})
            play sound "audio/sfx/click button.ogg"
            m "{glitch=50.0}{color=#0d0}실례합니다. 공항으로 가는 길이 어딘지 여쭤봐도 될까요?{/color}{/glitch}"
            jump s3_1

        "선택지 2 : OOOOOOOO?":  
            play sound "audio/sfx/click button.ogg"
            m "{glitch=50.0}{color=#0d0}생선이 참 튼실하네요! 천국 바다에서 잡은 생선 맞죠?{/color}{/glitch}"
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
    
    # 몸짓 효과음 추가(trembling.ogg)
    play sound "audio/sfx/trembling.ogg"
    #잠시 대기하는 연출 삭제(scene p3 pause 0.2 scene p3)

    "-휙. 휙."
    "난 하늘을 가리키고 비행기처럼 날개를 펼쳐 나는 시늉을 보였다."
    "허접하면서도 수치스럽긴 하지만, 어쩌겠어. 일단 이렇게라도 대화해야 길이 트이잖아."
    fish "...아! 니, 외국인이었나?"
    #대사 추가("가만 있자. 정류장이 분명...")
    fish "가만 있자. 정류장이 분명..."
    # 동작 단어 삭제('-스윽.')
    ch_na "다행히도 아줌마가 알아들으신 모양인지, 손가락으로 어딘가를 가리키셨다."
    fish "저그서 오는 버스를 타고 쭉 가믄 공항이 보일 기다. 거그서 내리면 된다."
    # 텍스트 글리치 효과 추가({glitch=50.0})
    m "{glitch=50.0}{color=#0d0}그렇군요, 감사합니다!{/color}{/glitch}"

    "가리키신 곳이 버스 정류장이었구나. 저기서 버스를 타면 되겠지?"
    "어디 보자, 정류장에 붙은 노선도를 보면... 그래, 저 번호가 적힌 버스를 타면 공항으로 갈 수 있겠구나."


label s4:
    scene p4 with dissolve # 버스 장면
    #버스 도착 효과음 추가(bus stop.ogg)
    play sound "audio/sfx/bus stop.ogg"
    "-끼익."
    "잠시 기다린 사이, 전광판에 307이라고 적혀있는 버스가 도착했다."

    "저 버스가 공항으로 간다고 노선도에 적혀있었으니 저걸 타면 될 거야."

    #잠시 대기하는 연출 삭제(scene p4 pause 0.3 scene p4)
    "- 삐~"
    "신호음과 동시에 버스 문이 열리자, 먼저 안에 올라타 자리에 앉으려 했다."

    #bus = 버스 기사
    #버스 경고 효과음 추가(bus horn.ogg)
    play sound "audio/sfx/bus horn.ogg"
    bus "저기, 손님!"
    ch_na "뭐야, 기사님이 갑자기 나를 보며 소리치시네."
    "내가 뭘 잘못한 게 있나, 왜 그러시는걸까?"
    bus "그냥 타시면 안 돼요!"
    ch_na "정말이지. 말이 안 통하니까 문제를 어떻게 해결해야 할지 모르겠네."
    "일단 기사님을 만나러 가봐야 되겠다. 무슨 의도로 말하는 지 알아먹어야 하잖아."

    # 걷는 효과음 추가(walk.ogg)
    play sound "audio/sfx/walk.ogg"

    #잠시 대기하는 연출(scene p4 pause 1.2 scene p4) - pause 0.2-> 1.2로 수정
    scene p4 
    pause 1.2
    scene p4
    "-스윽."
    "직접 대면하자, 기사님이 작은 모니터가 달린 기기와 돈을 넣는 투입구를 가리키셨다."
    bus "저기다 카드를 찍으시거나 여기 안에 돈을 넣으시고 타셔야죠."
    ch_na "아, 맞다. 왜 버스 요금을 생각 못했지."
    "근데 돈을 무슨 수로 내야 하나. 나 지금 한 푼도 없는데, 지금 당장 누구한테 빌려야 해?"
    "안돼, 그럴 수는 없지. 그냥 걸어가는 수밖에."
    "힘들겠지만 양심을 버리고 멋대로 탈 수는 없잖아."

    mys "아, 저기..."

    # 스포츠옷 노웰이 걸어오는 연출 추가
    show scg_nowell sports walk  with lefttoright

    "버스에서 내리려 마음먹던 순간, 어떤 청년이 버스 기사에게 말을 걸었다."

    bus "아는 사이이신가요?"
    # 노웰이 윙크하는 모습 추가
    show scg_nowell sports wink with fastdissolve
    mys "친구가 먼저 정류장에 자리를 잡고 있어가지고, 하하핫..."
    bus "아아, 알겠습니다."
    # 노웰이 숨는 모습 추가
    hide scg_nowell sports wink with dissolve
    ch_na "뭔 상황인지 모르겠지만, 일단 내려야겠지? 나랑은 상관없는 일이잖아."
    bus "손님! 타셔도 돼요!"
    ch_na "뭐야, 갑자기 기사님이 안으로 들어오라는 손짓을 하네. 타도 되는 거야?"
    bus "저분이랑 아는 사이 아니셨어요?"

    ch_na "버스 기사가 방금 요금을 낸 남자를 가리켰다." 
    "설마 저 남자가 내 버스비까지 내 준건가?"


label s5:
    scene p5 with dissolve  # 공항

    #버스 멈추는 효과음 추가(bus stop.ogg)
    play sound "audio/sfx/bus stop.ogg"
    ch_na "-끼익."
    "버스는 달리고 달려서 어느덧 공항으로 보이는 건물에 도착했다."
    "버스에서 내린 뒤 주위를 살펴보며, 내가 생각한 곳과 맞는지 분석해보았다."
    #비행기 효과음 추가(airplane.ogg)
    play sound "audio/sfx/airplane.ogg"
    "근처에서 비행기가 이륙하는 소리, 캐리어를 끌고 안으로 들어가는 다양한 인종의 사람들..."

    "그래, 확실히 공항인 것 같다. 조금 전 노선도로 봤을 때도 이 정류장에 비행기 마크가 붙어 있었잖아."
    #아래 두 문장 분리
    "좋아, 본격적으로 부딪혀볼까."
    "들어가서 후딱 끝낸 다음에 새로 터전을 찾으러 궁리해보자고."

    #eclipsy -> eclipsy3로 수정
    scene p5 with eclipsy3 #눈이 하얘지는 연출

    #음악 변경(warning.ogg) 및 효과음 추가(flash.ogg)
    play music "audio/music/warning.ogg" fadein 1.0
    play sound "audio/sfx/flash.ogg"

    "윽, 뭐야! 갑자기 눈이 왜 하얘져..."
    "목이 갑자기 조이고 있는 느낌이 들었다. 누가 이러는 거지?"
    #텍스트 글리치 추가
    m "{glitch=50.0}{color=#0d0}콜록, 콜록!{/color}{/glitch}"
    #쓰러지는 효과음 추가(body fall.ogg)
    play sound "audio/sfx/body fall.ogg"
    with Shake((0, 0, 0, 0), 0.4, dist=30)
    ch_na "계속 목이 졸리는 고통 속에, 나는 주저앉고 말았다."
    "호흡은 쉴 새 없이 가빠지고, 정신은 아늑해져 가고..." 
    "설마, 나 또 죽는 거야? 여기 온 지 얼마 됐다고?"
    "으으, 눈이... 점점 감긴다. "
    "천국에서 죽으면 난 대체 어디로 가는 거야..."
    #음악을 서서히 멈추는 연출 추가
    stop music fadeout 1.0




label s6:
    #eyeclose에서 eyecloseslow로 변경
    scene p6 with eyecloseslow

    mys "정신이 드나?"

    ch_na "서서히 의식이 다시 깨어나려 할 때, 소녀로 추정되는 목소리가 귓가에 들렸다."
    "여전히 무슨 말을 하는지 알 수는 없었지만, 그녀가 날 병원으로 데리고 온 건가?"
    #음악 추가(castle1.ogg)
    play music "audio/music/castle1.ogg" fadein 1.0

    #눈을 뜨는 연출
    # 리스 평상 시 -> (scg_reese normal -> scg_reese1으로 수정)
    show scg_reese1 with dissolve

    "그 목소리에, 나는 눈을 떴다."
    "근데 여기는 병원이 아닌데? 세련되면서도 고급져보이는, 귀족들이 지낼 것 같은 공간이잖아."
    "기절한 사이에 대체 무슨 상황을 겪은 거야, 난..."
    #아래 두 문장 삭제
    #"붉은 양갈래 머리에 검붉은 고스로리 드레스..."
    #"제법 화려한 차림을 한 듯한 소녀는 날 계속 응시하며 중얼거리고 있었다."
    "것보다 이 소녀는 뭐지? 왜 나를 이곳으로 옮긴 거야?"
    #텍스트 글리치 추가
    m "{glitch=50.0}{color=#0d0}당신은... 누구죠?{/color}{/glitch}"
    #리스 모습 변경(scg_reese1 shout)
    show scg_reese1 shout with fastdissolve
    mys "응? 희한하구마. 에르온에서 쓰는 말을 다 하고."
    ch_na "내가 소녀의 정체가 뭔지 물어보고 싶어도 대화가 안 통하네, 대화가."
    "이런 말을 꺼내는 내가 바보지."

    mys "후우..."

    # 리스 평상 시 걸을 때 -> (scg_reese normal walk -> scg_reese1 walk로 수정)
    #하이힐 걷는 효과음 추가(high hill walk.ogg)
    play sound "audio/sfx/high hill walk.ogg"
    show scg_reese1 walk with dissolve

    "검은 구두 소리와 함께, 소녀가 자기 손가락에 입김을 불며 나한테 다가왔다." 
    
    # 걷는 장면 숨기기 - 수정
    hide scg_reese1 walk
    with dissolve
    "무슨 의도로 오는 건지 모르니까 부담스러운데..."

    #때리는 효과음 추가(smash.ogg)
    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.4, dist=30)



    "-빠악!!"

    "아얏! 뭐야, 갑자기 내 이마에 왜 딱밤을 때리는 거지? "
    "이해가 안 가는 짓을 하네? 아으, 가뜩이나 머릿속이 복잡해 열날 지경인데."

    #scg_reese normal -> scg_reese1으로 수정
    show scg_reese1 with dissolve
    mys "마, 인자 내 말을 알아듣것제?"
    "어라, 갑자기.., 귀가 맑아진 느낌이 들어. 이제 저 소녀의 목소리도 똑바로 들리고."

    # 소리지르는 모습 추가(scg_reese1 shout)
    show scg_reese1 shout with fastdissolve
    mys "여그 말을 알아들을 수 있도록 마법을 걸었다카라. 동시에 니 말도 한국어로 들리게 해줬고. "
    m "한국어요...?"
    mys "기래, 한국에서 쓰는 언어다카라."

    #아래 두 문장은 삭제
    #with Shake((0, 0, 0, 0), 0.3, dist=20)
    #m " ...에에에에?!"

    "천국이 아니라 한국이라고? 잘못 들은 거지, 내가?"
    "사후 세계가 천국과 지옥말고 다른 데가 어디 있겠어?"

    mys "와 그리 놀라나?"
    m "혹시, 천국이라고 말씀하셨나요? 제가 말을 잘 못 알아 들어갖고..."
    # scg_reese1 shake close eyes 추가
    show scg_reese1 shake close eyes with fastdissolve
    mys "천국? 니, 가톨릭 신자가?"
    m "가톨릭? 이건 또 무슨 말이야. 신자라고 하는 걸 보면 종교 쪽인 것 같은데."
    m "그럼 여기가... 천국이 아니에요?"

    #당황하는 효과음 추가(silly.ogg)
    play sound "audio/sfx/silly.ogg"
    # 리스가 황당할 때 -> scg_reese confuse -> scg_reese1 silly로 수정
    show scg_reese1 silly with vpunch

    mys "뭔 소리를 하는 겨. 니 설마 사이비 놈들헌테 홀린 건 아니제?"
    m "저, 저 종교 안 믿어요! 사이비도 안 믿고요!"
    ch_na "머리가 점점 해탈해져 간다... 천국도 아니고 에르온도 아니면 여긴 어떤 세계인 거지?"

    show scg_reese1 with fastdissolve
    #대한민국 텍스트 강조 효과 추가
    mys "여긴 천국이 하니라 한국이다. 풀어서 말허믄, {color=#ff0000}대.{color=#5791FF}한.{color=#ff0000}민.{color=#5791FF}국{/color}{/color}{/color}{/color}이라고 혀지. 알아듣것나?"
    "한국이건 대한민국이건 간에 지금 그게 문제가 아니다."
    ch_na"나 분명 죽었을텐데. 심장 뚫려서 뒤졌잖아."
    "그럼 내가 있을 곳은 천국 아니면 지옥 아니야? 여긴 누가 있는 땅인데!"

    # scg_reese1 shake smile 추가
    show scg_reese1 shake smile
    mys "암튼, 여그는 처음이라 아직 적응이 잘 안 되제? 조만간 적응하믄, 괜찮아 질 기라."
    ch_na "원치도 않은 세계에서 발을 디뎠는데 지금 괜찮을 수가 있겠냐고!"
    "...일단 진정하자. 저 소녀한테 감사의 말부터 올려야지."
    m "아아, 네. 감사했습니다. 덕분에 잘 적응할 수 있을 것 같아요."

    ch_na "일단 여기서 물러나 앞으로의 계획부터 짜보자고. 내가 왜 여기 있는지부터 알아야 하니까."

    # scg_reese smile -> scg_reese1 close smile로 수정
    show scg_reese1 close smile with dissolve
    mys "감사혀야제. 앞으로 더 감사혀야 할 일이 많을 끼니."

    #음악 멈추는 효과 추가
    stop music fadeout 3.0

    ch_na"자, 잠깐... 불안하게 그건 또 갑자기 무슨 말이야."
    "저 소녀가 나한테 볼 일이 또 있는 모양인건가?"
    #심장 고동 음악 추가(heartbeat.ogg)
    play music "audio/music/heartbeat.ogg"
    show scg_reese1 with fastdissolve
    mys "잘 들으라. 그대는 이제부터..."

    #반짝이는 하이라이트 연출 추가(아래 5구문)
    stop music
    play sound "audio/sfx/shining.ogg"
    show scg_reese1 shout with eclipsy4
    pause 0.6
    mys "{size=+18}내 {color=#eaa6ff}집사{/color}가 되는 기라!"

    ch_na "..."

    "...응?"

    #프롤로그 종료(챕터 종료 시 scene black with eyecloseslow)
    scene black with eyecloseslow



#[챕터 1-1]

label chapter1_1:
    scene c1-1 with dissolve   #리스의 집
    

    play music "audio/music/castle2.ogg"
    m "...ㄴ, 네?!"
    ch_na "정말 어처구니가 없네. 방금 저 소녀가 한 말이 뭐라 했냐, 날 집사로 만들겠다?"
    "가만히 생각해보니까 쟤가 하는 말 하나하나가 믿기지를 않네. 무슨 말도 안 되는 소리를 자꾸 하는 거야, 저 애는." 
    "천국이 아니라 다른 세계라 그러고. 갑자기 날 집사로 부려 먹는다고 하고."

    show scg_reese1 shout with dissolve

    mys "니는 이제부터 내 집사라고. 알아들읏나?"
    m "무슨 소리를 하시는 거예요! 왜 제가 당신의 집사가 되어야..."
    # 리스 감은 표정 추가
    show scg_reese1 close eyes with fastdissolve
    mys "자세한 얘기는 나중에 한다카라. 일단은..."
    #아래 두 문장 분리
    m "일단은! 이유부터 말씀해주셔야 제가 납득이 가든가 하죠!"
    m "이렇게 나 몰라라 발뺌하시면..."
    # 효과음 + 표정 추가
    play sound "audio/sfx/mental crash.ogg"
    show scg_reese1 shout with vpunch
    #아래 두 문장 분리 및 수정
    mys "{size=+11}발뺌? 으디서 철이 덜 든 소리를...!"
    mys "이 자슥아, 나가 니 같은 사람 붙잡고 평생 노예처럼 부리먹는 줄 아나?"
    show scg_reese1 close eyes with fastdissolve
    ch_na  "이거 거의 노예계약 아니야? 맞잖아. "
    "이 여자, 날 구해준 게 아니라 붙잡은 거네! 어쩐지 왜 여기로 왔나 했더니..."
    "얼른 여기서 벗어나야지. 저 사람이랑 붙었다가는 평생 고생길을 면치 못할 거야."
    mys "한 번 도망쳐봐라. 소용 읎는 짓이긴 하겠지만은."
    hide scg_reese1 close eyes with fastdissolve

    #아래 두 문장 분리 및 효과 추가
    m "뭐가 소용이 없..."

    # 구속 마법에 걸린 연출(shake 효과 적용) - 효과음 및 연출 추가
    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "윽!"


    ch_na "몸을 겨누려 하는데 움직이지를 않아? 뭔 짓을 한 거야?"
    #배경 붉게 하는 연출 추가
    scene c1-1 with dissolve:
        matrixcolor TintMatrix("#800000") * SaturationMatrix(0.5)  
    play sound "audio/sfx/reese magic.ogg"
    show scg_reese1 close eyes with dissolve
    mys "것 참, 안 부리먹는다고 혔는데."
    m "안 부려먹는다 하면서 이런 행동을 하세요?"
    mys "발뺌할 생각은 말라는 차원에서 구속 마법을 걸었다카라. 이 근방에서는 어디 있는지 다 알 수 있으니."
    ch_na "제기랄, 구속 마법이라니 재수 옴 붙었구만."
    "하필이면 저런 악덕 같은 사람한테 거두어졌지?"
    #배경 원래대로 하는 연출 추가
    show c1-1 behind scg_reese1 with dissolve:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)  
    # 리스가 황당할 때 -> scg_reese confuse - 수정
    show scg_reese1 shout with dissolve
    mys "방금 행동을 보니 내 집사가 되는 게 별 관심이 읎는 모양이구마."
    m "이유를 말씀해주시질 않으시니 그런 생각을 할 수밖에 없잖아요! 말씀해보세요, 제가 왜 당신 밑으로 들어가야 하는..."

    #[화면이 흔들리는 연출] - 추가
    show scg_reese1 close eyes
    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    
    ch_na "내가 이유를 물으려고 하니 다시 딱밤을 불날 듯이 때리네, 아파라..."
    mys "가마이 있으라. 증말이지 말해줄 때가 있다고 처음에 한 번, 조금 전에 또 한 번 말했는디."
    # 소리지르는 표정 추가
    show scg_reese1 shout with fastdissolve
    mys "와 이리 고집부리고 난리인기라?"
    m "아, 알겠습니다..."
    ch_na "일단 저 사람의 말을 들어야 할 것 같네. 이 이상 들이대도 도저히 말이 통하지 않을 거야."
    # 표정 수정(normal -> close eyes)
    show scg_reese1 close eyes with fastdissolve

    # 아래 구문 대촉 수정(색깔, 표정 추가 등)
    mys "주종 관계로서 정식으로 인사를 올려야긋제?"
    "내 이름은 {color=#ff0000}사투 리스{/color}. 뱀파이어 혈통으로 이루어진 사투 가문의 귀족인기라."
    #아래 두 문장 분리
    ch_na "{color=#ff0000}사투, 리스...{/color}"
    "그래. 사투리스는 뱀파이어라..."
    show scg_reese1 shout with fastdissolve
    r "그쪽 이름은 어케 되나?"
    #$ povname = renpy.input("이름을 적어주세요.", length =40) 
    #my "{color=#0bb9d8}[povname]{/color}라고 합니다."
    m "{color=#0bb9d8}매시안 크리스토프{/color}라고 합니다."
    show scg_reese1 close eyes with fastdissolve
    r "그렇구마. 딱 봐도 내랑 나이는 별 차이 없는 거 같고."
    ch_na "그럼 이 소녀도 나랑 같은 성인인 건가? 체형이 제법 있는 걸 봐선 그럴 지도..."
    m "실례지만, 혹시 나이가 어떻게..."
    show scg_reese1 smile with fastdissolve
    r "20살인기라. 인자 성인이 된 기분이 막 드는 나이제."
    ch_na "20이라고 한다면 성인이잖아? 그럼 술도 들이키고 하겠네."
    "나중에 잔뜩 취하거나 한다면 뒤처리도 해야 하고... "

    #음악 멈춤 추가
    stop music fadeout 1.0
    show scg_reese1 shout with fastdissolve
    r "자, 통성명도 마쳤으니 가사 활동을 시험혀 봐야겄네."
    m "가사... 활동이요?"
    r "기래. 집사가 됐으믄 집안일 실력이 으뜬지 한 번 봐야하니."
    label text11:
    #음악 재생, 표정 다수 추가
    play music "audio/music/castle3.ogg" fadein 0.5
    ch_na "마, 맞는 말이긴 하지, 집사는 주로 가사 활동에 충실해야 하니까. 고된 시간이 되겠네."
    show scg_reese1 shake smile with fastdissolve
    play sound "audio/sfx/cloth wear.ogg"
    r "먼저 청소기로 성 안에 있는 모든 먼지를 다 쓸어뿌라. 말 잘 듣는 놈이니 안 빨릴 거란 걱정은 말고."
    show vacuum cleaner at right2 with dissolve
    ch_na "이 넓은 데를 나 혼자 쓸으라고? 합해도 한 60평은 넘어 보이는데, 여기?"
    r "와 그리 놀라나? 무슨 문제라도?"
    m "당연하죠! 이 넓은 데를 어떻게 혼자서..."
    play sound "audio/sfx/silly.ogg"
    show scg_reese1 silly smile with fastdissolve
    r "또 맞아야 정신을 차리것네."
    m "번복할게요! 당연히 할 수 있죠! 헤헤..."
    show scg_reese1 close eyes with fastdissolve
    r "...정신 좀 차리라, 이래가지고 집사 일을 어떻게 하긋냐?"
    ch_na "한숨이 절로 나올 것 같지만, 이 이상의 독설을 듣기는 무리니까..."
    $ persistent.sit[0] = 100 # 기운을 초기화 합니다
    jump My_home1

label chapter1_1_c:
    #선택지 - 효과음 및 포인트(Test_Point) 추가
    play sound "audio/sfx/select button.ogg"
    hide vacuum cleaner with dissolve
    menu:
        "선택지1 : 후딱 끝내자.":  
            play sound "audio/sfx/click button.ogg"
            jump chapter1_1_a
            

        "선택지2 : 힘 좀 들겠지만 꼼꼼하게 끝내는 게 좋겠지.":  # 스테미나 -3
            play sound "audio/sfx/click button.ogg"
            $ Test_point += 1
            jump chapter1_1_b

# 선택지 구문 둘 다 대폭 수정(스크립트 수정 및 효과음 추가 등)
label chapter1_1_a: # 후딱 끝내자
    ch_na "보이는 것만 쓸고 끝내는 게 낫겠다. 혼자서 이 넓은 데를 어떻게 꼼꼼히 보겠어."
    "어디 보자, 먼지가 제일 많이 생길 만한 곳이... 그래, 이쪽이랑 저쪽만 인지하면 되겠다."
    "옷장이나 냉장고 근처는 신경 쓰기 힘들겠지. "
    "옷 갈아입어야 하고, 음식 꺼내야 하고... 먼지를 어케 신경 쓰겠니. "

    play sound "audio/sfx/cleaning.ogg"
    "-위이이잉~" # [청소기 효과음]
    "쓸면서 보니까 그리 먼지가 많이 보이지도 않네. 내가 너무 호들갑을 떨었나?"
    "좋아, 금방 끝낼 것 같은 느낌이 들어!"

    scene black with dissolve

    "- 약 1시간 뒤 -"

    scene c1-1 with change007

    m "후우..."
    ch_na "끝났다. 대청소의 대장정이 드디어 막을 내렸다."
    "이제 한숨 푹 돌려도 되겠지."
    show scg_reese1 shout with dissolve
    r "다 했나?"
    m "끝났어요! 퍼펙트하게요!"
    ch_na "감이 왔다. 이건 무조건 합격이다."
    "적어도 이걸로 불평들을 일은 무조건 없을 거란 징조가 왔지."
    show scg_reese1 close eyes with fastdissolve
    r "증말 니 말대로 퍼팩트하게 다 됐는지 한 번 볼까?"
    ch_na "리스가 청소했던 부분을 꼼꼼히 살피기 시작했다."
    "백날 찾아봐라. 먼지가 한 톨이라도 보이겠냐?"
    play sound "audio/sfx/mental crash.ogg"
    show scg_reese1 shout with vpunch
    r "{color=#fff000}마, 집사!!{/color}"
    ch_na "어라? 리스가 날 바라보는 눈빛이 예사롭지 않네..."
    "뭔가 문제라도 있나?"
    r "퍼펙트는 무슨 얼어죽을! 여그 청소가 똑바로 안 됐잖나!"
    r "눈 똑바로 뜨시고 한 그 맞나?!"
    m "분명 청소했던 곳인데..."
    play sound "audio/sfx/hammer.ogg"
    show scg_reese1 silly smile with vpunch
    r "구라치지 마라! 여그도 저그도 다 보이는디! 대충대충 혀면 나가 그냥 넘어갈 줄 알앗나?!"
    ch_na "실수가 좀 있었구만. 피땀 흘려가면서 미친 듯이 쓸었는데..."
    "대충 한 대가는 참으로 쓰게 오네. 생각 외로 꽤 꼼꼼한 것도 의외였어." 
    "아님 내가 멍청했을지도. 변명이 오히려 독이 된 꼴이야."
    m "...눈깔을 굴리는 훈련이 부족했나 봅니다."
    ch_na "잘못을 범한 내게 해야 할 행동은 고개를 숙여 사과하는 것 뿐이지. 이외의 선택지는 전무하니까." 
    show scg_reese1 close eyes with fastdissolve
    r "인자 주방으로 와보라. 요리를 한 번 볼 티니."
    jump chapter1_1_2

label chapter1_1_b: # 꼼꼼하게 끝내자
    ch_na "그래, 내가 청소 경력이 얼마나 되는데 이깟 거 못하겠냐."
    "각오해라, 먼지들아! 용병 시절 수 년간 겪었던 청소 경험으로 너희를 모두 쓸어버릴테니!"
    play sound "audio/sfx/cleaning.ogg"
    "-위이이잉~" # [청소기 효과음]
    "난 무선청소기의 전원을 켜 각 방과 거실, 주방 등 고성 곳곳을 쓸기 시작했다."
    "한 톨의 먼지도 보이지 않도록 안 보이는 데까지 꼼꼼하게! 잘 안 쓸리는 먼지가 있다면 걸레로 한 번 닦아주고!"
    "그, 근데 몸이 예전같지가 않네. 방금 허리를 삐끗할 뻔했어..."
    scene black with dissolve

    "- 약 1시간 뒤 -"

    scene c1-1 with change007
    show scg_reese1 close eyes with fastdissolve
    r "으음... 뭔 꼼수라도 부린 기가, 안 보일 리가 없는디..."
    ch_na "아직 내 청소 실력을 인정하지 못한 모양이구만."
    "현미경을 써도 소용없어요. 그 전에 내가 청소 점검을 몇 번이나 했는데."
    show scg_reese1 silly smile with fastdissolve
    r "크, 크흠... 잘혔구마. 의외로 그런 구석이 있을 줄은 몰랐는디."
    ch_na "꼼꼼한 면은 집사의 필수사항 아니겠어."
    "뭐, 내가 아직 이런 직종을 잘 모르긴 하지만. 틀린 말은 아니지." 
    show scg_reese1 close eyes with fastdissolve
    r "좋아, 인자 주방으로 와보라. 요리를 한 번 볼 티니."
    jump chapter1_1_2

label chapter1_1_2:
    scene c1-2 with change007

    ch_na "이번에는 주방 쪽만 움직이니 청소할 때보단 덜 걷겠네."
    "근데 어쩌면 청소보다 더 힘들 수도 있겠어. 요리란 게 손맛을 크게 타는 일이잖아."
    show scg_reese1 close eyes with fastdissolve
    r "냉장고 안에 필요한 재료는 다 있을 기니, 맛난 걸로 알아서 만들라."
    m "알겠습니다."
    hide scg_reese1 close eyes with fastdissolve
    play sound "audio/sfx/fridge open.ogg"
    ch_na "-덜컥."
    "3개로 이루어진 냉장고 문을 모두 열었더니 각양각색의 재료들이 다 있네. "
    "한쪽은 고기, 다른 한쪽은 해산물과 채소가 있고... "
    "일단 식재료가 다 좋아 보여가지고 괜찮네. 웬만한 음식들은 다 만들 수 있을 것 같아."
    "취사담당이 있었던 병사 시절 이후에는 요리를 자주 하지 않았지만..."
    "그 때 기억이라도 한 번 살려보도록 하자고."

    #선택지
    play sound "audio/sfx/select button.ogg"
    menu:
        #선택지 구문  대폭 수정
        "선택지1 : 레스토랑 풍의 스테이크":  
            play sound "audio/sfx/click button.ogg" 
            jump chapter1_1_2_a

        "선택지2 : 매운 향이 가득한 볶음밥":  
            $ Test_point += 1
            $ Cook_point += 1
            play sound "audio/sfx/click button.ogg"
            jump chapter1_1_2_b

label chapter1_1_2_a: # 스테이크
    ch_na "일단 가장 생각나는 건 케이크 종류의 디저트 아님 스테이크인데..."
    "내가 베이킹을 해본 적은 거의 없었지. 어렸을 때 체험식으로 해본 걸 빼면."
    "그럼 스테이크로 가자. 요리 잡지에서 봤던 레시피가 있었으니, 그 기억을 되살리면 될 거야."
    "우선 두툼해 보이는 고기부터 밑간하는 걸로 시작해볼까. "
    "저 작은 병 안에 든 가루가 시즈닝할 때 쓰는 거겠지. 그걸 고루 뿌려주고..."
    "간이 베이는 동안 채소를 손질하면, 모든 준비가 끝나는 거다. 이제 팬을 꺼내 굽는 일만 남았네."
    play sound "audio/sfx/holding pan.ogg"
    "-스윽."
    "어우, 이 팬 생각보다 묵직하네. 그쪽 세계에 썼던 건 이보다 훨씬 가벼웠는데."
    "어쨌든 고기를 구워보자고. 이 V자형으로 생긴 게 아마 고기를 뒤집는 거겠지."
    "팬에 기름을 넉넉하게 둘러 뜨겁게 달궈준 다음에 연기가 올라오면은..."
    play sound "audio/sfx/grill.ogg"
    "-촤르르르~" #[고기 굽는 효과음]
    "크으! 이 소리 참 간만에 들어본다. 팍 터지면서도 자글자글거리는 순간을 누가 안 좋아하겠어?"
    "아, 그러고 보니 굽기 정도도 생각해야 해. 한 미디움 정도면 되겠지?"
    "좋아, 이제 뒤집어볼까. 어떻게 구워졌나..."
    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "...으앗!"
    ch_na "세, 세상에. 표면이 모두 검게 타버렸잖아!"
    "분명 이때 뒤집는 게 맞았을 텐데. 내가 시기를 잘못 계산했나?"
    "아이 씨, 망했다! 이걸 어떻게 꼼수라도 부릴 수 있나."
    "이, 일단 다 굽고 나서 검은 부분만 손질하든가 하자고... 그 외에는 별문제가 없겠지?"

    scene black with dissolve

    "- 잠시 후 -" #[화면이 꺼졌다가 다시 켜지는 연출]

    scene c1-2 with eyeclose

    play sound "audio/sfx/plate.ogg"

    m "완성됐습니다, 드셔 보세요."
    show scg_reese1 little smile with fastdissolve
    r "오오, 스테이크라... 눈치 하나는 좋네."
    ch_na "한땀한땀 정성들여 플레이팅한 스테이크를 리스가 넋 놓으며 들여다보고 있었다."
    "일단 첫인상은 좋구만. 잠깐 한숨이 놓이네."
    r "비주얼은 괜찮아 보이는구마. 그럼 한 번 먹어볼까나..."
    play sound "audio/sfx/knife.ogg"
    ch_na "-슥슥."
    "리스가 나이프로 스테이크를 썰어 맛볼 준비를 하기 시작했다."
    "고기 단면은... 어라, 속이 완전히 익어버렸는데? 내가 생각한 미디움은 아닌 걸..."
    show scg_reese1 close eyes with fastdissolve
    r "아음..."
    ch_na "한 입 크기로 잘 썰어가지고 입 안에 넣었네."
    "그래도 밑간은 적당히 했으니 적어도 고기 맛은 보장되어 있겠지." 
    show scg_reese1 shake close eyes with fastdissolve 
    r "으응...?"
    ch_na "아 이런,  표정을 살짝 찌푸렸는데, 고기에서도 문제가 있나?"
    show scg_reese1 sad with fastdissolve 
    r "아우, 너무 질기구마... 고무를 씹는 느낌인데."
    ch_na "역시 고기가 탔을 때가 불안하다 싶더니, 이렇게 정곡을 찌르네."
    "근데 솔직히 내가 100%% 잘못한 건 아니라고 생각하는데, 일단 이쪽 기름과 내가 살던 곳의 물건이 똑같겠어?"
    r "간도 참 씨게도 짜게 혔구마. 물 좀 실컷 마셔야 쓰것다카라."
    ch_na "시즈닝도 별로라고? 제일 중요한 고기 맛도 망쳐버리다니... "
    "이거 평가가 애매하겠네. 접시 세팅은 제법 잘 한 것 같은데."
    show scg_reese1 close eyes with fastdissolve
    r "아무래도 요리 경험은 별로 없는 것 같구마. 요걸 읽으면서 배워야 쓰것다."
    ch_na "리스가 고개를 저으며 건네준 책은 요리책이었다. "
    "'초보자도 레스토랑 음식을 만드는 비법!'이라... 그래, 나 아직 초짜다."
    "갈고 닦아야지 뭐, 그럼 어쩌겠어. 또 이렇게 만들면 불만이 계속 샐 텐데."
    stop music fadeout 1.0
    jump chapter1_1_3  #[선택지1 구문 종료]


label chapter1_1_2_b: # 볶음밥
    ch_na "어쩌면 이런 간단히 만들 수 있는 음식이 오히려 좋은 반응을 받을 수도 있어."
    "귀족이 항상 금가루 들어간 음식만 먹지는 않잖아. 축제 때 길거리에서 꼬치 같은 걸 사 먹는 귀족들도 봤는데."
    "그래, 이게 그나마 가장 자신있어하는 음식이니 그걸로 가보자."
    "고기와 야채를 잘게 다지고, 밥과 함께 프라이팬에 넣은 뒤..."
    play sound "audio/sfx/grill.ogg"
    "매콤한 소스를 넣고 불맛이 나도록 센 불로 빠르게 볶아주었다."
    "볶으면서 나는 향이 굉장히 좋네. 살짝 맛을 보니 간도 잘 배여 있고."
    "맵찔이가 아닌 이상 이걸 리스가 안 좋아할 수 없겠지."
    scene black with dissolve

    "- 잠시 후 -" #[화면이 꺼졌다가 다시 켜지는 연출]
    #[화면이 꺼졌다가 다시 켜지는 연출]
    scene c1-2 with eyeclose

    play sound "audio/sfx/plate.ogg"
    m "완성됐습니다, 드셔 보세요."
    show scg_reese1 little smile with fastdissolve
    r "으음, 볶음밥이가? 좋은 향이 도는구마."
    ch_na "리스가 볶음밥이 담겨있는 접시를 보며 고개를 끄덕였다."
    "제법 평범한 음식이라 살짝 걱정은 됐었는데, 예상외로 괜찮은 반응이라 다행이네."
    r "자, 한 번 먹어볼까나... "
    show scg_reese1 close eyes with fastdissolve
    play sound "audio/sfx/spoon.ogg"
    ch_na "-덥석."
    show scg_reese1 little smile with fastdissolve
    "리스가 숟가락으로 볶음밥을 퍼 한 입 덥석 물었다."
    "과연 이걸 먹고 어떤 소감을 말할지..."
    show scg_reese1 shake smile with fastdissolve
    r "오호라! 맛이 아주 기가 맥히는데?"
    r "진하게 매운 향과 감칠맛이 감돈다카라!"
    ch_na  "후우... 다행히도 좋아해 줘서 고맙네."
    "내가 만들어준 음식을 먹고 맛있다고 하면 평가는 뻔하지."
    r "이 정도면 합격점을 줘도 되겄구마. 잘헛다. 음식 솜씨가 괜찮구마."
    m "감사합니다."
    ch_na "평가 후에도 리스는 계속 감탄을 자아내며 볶음밥을 계속 흡입했다."
    "밥 한 톨도 남기지 않고 먹는 걸 보면 이런 걸 좋아하는 모양이네. 원래 저런 음식을 자주 즐겨 먹나?"
    show scg_reese1 with fastdissolve
    r "근데 니,  다른 요리도 할 줄 아나?"
    m "다른 음식도 어느 정도 만들 줄 알지만..."
    m "고급 식당에서 나올 법한 비싼 음식들은 만들어보질 못했죠."
    r "기럼... 요게 도움이 될 지도 모르겄구마."
    r "틈날 때마다 함 읽어보라."
    ch_na "리스가 내게 한 권의 책을 건네주었는데, 요리책이네. 표지에 음식들로 가득 차 있으니까."
    "'초보자도 레스토랑 음식을 만드는 비법!'이라... 그래, 시간날 때 비법을 확실히 전수받아 보자고."
    stop music fadeout 1.0
    jump chapter1_1_3 #[선택지2 구문 종료]

label chapter1_1_3:
    scene c1-1 with dissolve   #리스의 집

    m "하아... "
    r "테스트는 모두 끝났다카라. 수고혔다."
    play music "audio/music/castle2.ogg" fadein 0.5
    ch_na "빨래, 정원 관리 등을 더 거치고 난 다음에야 모든 테스트를 끝마칠 수가 있었다."
    "테스트라는 게 이렇게 길었나. 기사단의 입단 시험도 이 정도까지는 아니었는데 말이다."

    #테스트 결과에 따라 스크립트 달라짐(추가)
    if Test_point  == 1:
        jump chapter1_1_3b

    elif Test_point == 2:
        jump chapter1_1_3c

    else:
        jump chapter1_1_3a

    #[청소 - 선택지1, 요리 - 선택지1 선택 시의 구문]

    
label chapter1_1_3a:
    show scg_reese1 sad with dissolve
    r "...뭐, 말 안 혀도 알긋제?"
    m "...네."
    r "집사라 부르기에도 민망할 정도였다카라. 발전하는 데 시간이 꽤나 걸리겄어."
    "전체적으로 나사가 빠진 부분이 많기는 했어. 아직 여기에 온 지 얼마 안 돼 마음이 복잡했던 부분도 있었고..."
    "이 악물고 발전하도록 노력해야지. 여기가 밑바닥이라 생각하고 갈고닦아보자."
    show scg_reese1 close eyes with fastdissolve
    r "정신 차리고 일로 오도록."
    $ persistent.sit[1] -= 1
    $ some_condition = False
    play sound "audio/sfx/rank down.ogg"
    show screen stat_overlay
    ch_na "{color=#0d0}정보 : 신뢰도({image=gui/handshake.png})가 1 감소하였습니다... {/color}"
    hide screen stat_overlay
    jump chapter1_1_4

    #[청소 - 선택지2, 요리 - 선택지1 선택 시의 구문]
    #혹은 [청소 - 선택지1, 요리 - 선택지2 선택 시의 구문]
label chapter1_1_3b:
    show  scg_reese1 with dissolve
    r "대략 요약하자믄, 괜찮은 부분도 있고 마음에 안 드는 부분도 있어 아주 좋은 점수를 주기는 힘들 것 같구마."
    r "뭐가 원인인지는 잘 알긋제?"
    m "그런 부분은 반드시 고쳐보도록 노력하겠습니다."
    ch_na "중간마다 리스의 지적을 피해 갈 순 없었지만, 그럭저럭 잘 진행된 것 같았다. "
    "정말이지, 이 세계에 오면서 처음으로 숨 막히는 순간들이었어."
    show scg_reese1 little smile with fastdissolve
    r "기래, 저런 말이 나와야 믿음직스럽지. 일로 오라."
    $ persistent.sit[1] += 1
    $ some_condition = False
    show screen stat_overlay
    play sound "audio/sfx/rank up.ogg"
    ch_na "{color=#0d0}정보 : 신뢰도({image=gui/handshake.png})가 1 증가하였습니다! {/color}"
    hide screen stat_overlay
    jump chapter1_1_4

    #[청소 - 선택지2, 요리 - 선택지2 선택 시의 구문]
label chapter1_1_3c:
    show scg_reese1 little smile with dissolve
    r "증말로 내가 딱 원했던 부류였다카라. 매사에 꼼꼼하고 집중하는 모습 하나는 마음에 든다. 성격만 살짝 고친다면..."
    m "아아, 그건 제가..."
    show scg_reese1 shake smile with fastdissolve
    r "내도 안다. 아직 여그로 온 지 얼마 안 됐으니 예민할 수밖에 없겄제."
    "내가 평소에는 성격이 그리 거칠지 않은 편이다. 부하들을 훈련이나 전투 등의 상황에서 막 함부로 대하지 않았고."
    "이 세계에서 워낙 황당한 일들을 많이 겪다 보니 잠깐 정신이 안드로메다로 간 거지. "
    "아무리 긍정적인 사람이라도 이런 일들을 한꺼번에 겪으면 감당하기가 정말 힘들 거야."
    "그걸 이해해주는 걸 보니까 살짝 마음의 문이 열리네, 안도감이 들어."
    r "자, 일로 오라, 믿음직한 집사여. 기막힌 걸 보여줄 티니."
    $ persistent.sit[1] += 2
    show screen stat_overlay
    play sound "audio/sfx/high rank up.ogg"
    ch_na "{color=#0d0}정보 : 신뢰도({image=gui/handshake.png})가 2 증가하였습니다! {/color}"
    hide screen stat_overlay
    jump chapter1_1_4
    
    #[선택지 구문 종료]


label chapter1_1_4:
    stop music fadeout 1.0
    scene c1-3 with dissolve   #매시안의 침실

    play sound "audio/sfx/door open.ogg"
    ch_na "-끼익." #[문 여는 효과음]
    show scg_reese1 little smile with dissolve
    play music "audio/music/castle1.ogg" fadein 0.3
    r "실컷 구경해보라. 여그가 앞으로 집사가 지낼 곳이니."
    hide scg_reese1 little smile with dissolve
    m "우와..."
    ch_na "리스가 문을 열어 나한테 보여준 건 입이 쩍 벌어질 정도로 널찍한 공간을 가진 방이었다."
    "거대하고 푹신해 보이는 침대도, 경치가 탁 트인 창문도 있다니. "
    m "여, 여기서 지내면 됩니까? 정말로요?"
    show scg_reese1 little smile with fastdissolve
    r "앞으로 계속 내와 지내는데 이 정도 공간은 제공해줘야제."
    ch_na "이 정도면 기사단에서 지냈던 숙소보다 훨씬 좋잖아?"
    "병사 시절에 동기들이랑 좁은 곳에서 다 같이 지냈던 것 생각하면, 이런 공간은 내게 큰 축복이나 다름없지."
    show scg_reese1 shake happy with fastdissolve
    r "흐흐, 놀랄 먼 하네. 이런 방은 귀족이나 대기업 회장 같은 사람들만이 지내는 곳이니."
    m "딱 봐도 그래 보이더라고요."
    ch_na "역시 귀족은 귀족이구나. 방 하나하나가 오피스텔 한 채 갖다 놓은 것 같다니까." 
    show scg_reese1 little smile with dissolve
    r "어이, 집사."
    m "네."
    r "인자 내한테 말 놔도 된다. 물어볼 게 있음 편하게 대답하고."
    m "어, 정말로요?"
    r "기래, 나이 차도 별 안 나고 어느 정도 같이 있을 사이인디, 존칭은 어색하다고 느껴지지 않나?"
    r "해보고 싶은 말이 있음 해보라. 함 들어는 봐주마."

    play sound "audio/sfx/select button.ogg" 

    
    #선택지 구문 대폭 수정(효과음 및 연출 추가)
    menu:
        "선택지1 : 잘 자": 
            play sound "audio/sfx/click button.ogg" 
            jump chapter1_1_4_a

        "선택지2 : 이 나쁜 X":  
            play sound "audio/sfx/click button.ogg" 
            jump chapter1_1_4_b

        "선택지3 : 고마워":  
            play sound "audio/sfx/click button.ogg" 
            jump chapter1_1_4_c

label chapter1_1_4_a: # 잘 자 선택

    m "피곤할 텐데 얼른 자. 고생 많았어."
    show scg_reese1 close smile with fastdissolve
    r "...기래. 니도 피곤할 틴디 푹 쉬고."
    "깜깜해진 지 한참 됐으니 저런 말을 건네주는 게 맞는 일이겠지. 눈이 침침해 보이는 것 같기도 하니."
    stop music fadeout 1.0
    jump chapter1_1_4_ #[선택지1 구문 종료]
 
label chapter1_1_4_b: # 쓰레기 같은 X 선택

    with Shake((0, 0, 0, 0), 0.3, dist=20)
    m "이 납치범 녀석! 감히 날 여기에 가두려 하다니, 내가 가만히 있을 줄 알아?!"
    show scg_reese1 silly smile2 with fastdissolve
    r "..."
    ch_na "후아, 속이 다 시원하네. 이런 말을 꼭 해보고 싶었거든."
    "그동안 날 계속 갈궜겠다? 그럼 이것도 맞받아 쳐보시지 그래? "
    "아이고, 화났어요? 화나면 뭐 어쩔 건데? 열불내는 거 말고 네가 뭘 할 수 있는..."
    r "이 빌어먹을 놈이 그냥...!"
    #[화면이 흔들리는 연출 x2]
    play sound "audio/sfx/smash.ogg" 
    with Shake((0, 0, 0, 0), 0.4, dist=20)
    play sound "audio/sfx/smash.ogg" 
    with Shake((0, 0, 0, 0), 0.4, dist=20)
    play sound "audio/sfx/smash.ogg" 
    with Shake((0, 0, 0, 0), 0.4, dist=20)
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
    #[화면이 격하게 흔들리는 연출]
    play sound "audio/sfx/smash.ogg" 
    with Shake((0, 0, 0, 0), 0.8, dist=40)
    m "끄에에에에에엑!!"
    ch_na "...멱이 따이는 기분이네. 으으..."
    "난 혹이 난 머리를 쓰다듬으며 고통이 빨리 해소되길 빌었다."
    "내가 너무 리스를 얕본 것 같아. 앞으로는 좀... 조심해야겠네."
    scene black with dissolve
    scene c1-3 with eyeclose
    stop music fadeout 1.0
    jump chapter1_1_4_ #[선택지2 구문 종료]


label chapter1_1_4_c: # 고마워 선택

    m "그럼 감사인사를 할게. 살 길을 트이게 해준 건 고맙다고 생각하고 있어."
    show scg_reese1 silly smile2 with fastdissolve
    r "어... "
    ch_na "갑작스런 감사인사에 리스가 어색한 표정을 지으며 얼굴을 살짝 붉혔다."
    "여기까지 오며 뭐 찔리는 거라도 있어서 그런 건가. "
    "하긴, 독설을 밥 먹듯이 한 게 가장 생각났을지도 모르겠지."
    r "기렇게 생각한 이유라도 있나?"
    m "그렇지 않았음 계속 떠돌이짓을 했겠지. 낙오된 외국인이나 다름없잖아, 내가."
    show scg_reese1 close eyes with fastdissolve
    r "으, 으흠... 맞는 말이긴 혀지."
    ch_na "잡혀있는 신세일지라도, 일단 이 세계에서 정상적으로 지낼 수 있게 해줬다는 건 사실이니까."
    stop music fadeout 1.0
    jump chapter1_1_4_ #[선택지3 구문 종료]



#아래 스크립트 대폭 수정
label chapter1_1_4_:
    show scg_reese1 close smile with dissolve
    play music "audio/music/castle2.ogg" fadein 1.0
    r "자, 내는 가보겠다카라. 내일 보자고."
    hide scg_reese1 close smile with dissolve
    play sound "audio/sfx/close door.ogg"
    "드디어 다사다난했던 하루가 막을 내렸네."
    "갑자기 한국이란 땅에 오지 않나, 여기로 끌려오지 않나, 여고생 뻘 되는 애의 집사가 되지 않나..."
    "오늘 경험한 것들은 다시 생각해도 이해할 수가 없는 일이었다."
    "내게 지금 무슨 일이 일어난 건지 모르겠어. 이걸 좋아해야 할지, 싫어해야 할지."
    "...일단 목욕부터 할까. 뜨거운 욕조에 담가 밝은 미래를 향한 망상이나 취해봐야지."
    with Shake((0, 0, 0, 0), 0.3, dist=40)
    m "...으엣!"
    ch_na "장갑을 떼는 순간, 난 내 손을 보며 화들짝 놀랐다."
    "보통 사람들의 피부는 살구색 아니야? 어떻게 내 손이 하얄 수가 있지?"
    "그럴 리가 없어. 손에 뭐가 칠해진 게 분명할 거야. 화장실로 가서 손을 닦으면 되겠지."
    m "에에에엣?! 이, 이게 뭐야?! "
    ch_na "화장실에 놓인 거울에서 얼굴을 보자마자, 난 또 경악할 수밖에 없었다."
    "얼굴 피부도 손과 마찬가지로 하얀색으로 뒤덮였으니까."
    "갑자기 왜 이렇게 변할 걸까? 다른 세계로 넘어온 영향인 건가?"
    "가만, 그럼 내 온몸도 그렇게 덮여 있지는..."
    m "..."
    ch_na "예상은 정확했다. 옷을 다 벗은 후에 봤을 때도, 머리부터 발끝까지 모두 하얀색으로 되어 있어."
    "맙소사, 온몸을 보니 내가 지금 사람이 아닌 외계인인 것 같잖아."
    "그냥 전부 다 페인트로 칠한 거라 믿고 싶어. 그래, 목욕을 해보자!"
    
    scene bathroom night with dissolve:
        matrixcolor TintMatrix("#ffdffb") * SaturationMatrix(0.5)

    play sound "audio/sfx/shower.ogg"
    "-쏴아아아." #[욕조에 물을 붓는 효과음]
    "뜨거운 물을 받은 욕조에서 몸을 담그고, 시간이 됐다 싶으면 때를 벗긴 다음..."
    "샴푸랑 바디워시를 이용해 온몸을 닦아서 하얀색 피부를 원래의 살구색 피부로 바꾸려 애를 썼다."
    "좋아, 이렇게 하면..."
    with Shake((0, 0, 0, 0), 0.3, dist=40)
    ch_na "칫, 괜시리 기대했나. 목욕하는 거로도 바뀌지 않네."
    "괜한 헛수고일 뿐이었구만..."
    "이 모습으로 계속 살아가야 한다고? 갑자기 눈앞이 막막한데."
    scene c1-3 with dissolve
    "피부에 너무 충격을 받은 탓인지, 한동안 침대에 주저앉아버렸다."
    "도대체 내가 왜 이리됐을까. 내 피부가 약한 것도 아닌데."
    "그 생각에 나는 도저히 잠이 오질 못했어... 아니, 잠이 오지 못했기보다는 잠이 아예 안 왔지."
    "이것도 무슨 이유인지는 모르겠지만, 피곤하다는 생각이 눈곱만큼도 들지 않았다. "
    "내 몸 상태가 어떤지를 모르겠네. 이상현상이 생긴 게 분명한데, 그 이유를 알 수가 없어."
    "정말이지,  왜 이렇게 꼬이는 거냐..."
    stop music fadeout 1.0
    scene black with eyecloseslow

    "챕터 2 : 적응기"


#[챕터 1-2]
label chapter1_2:

    scene c2-1 with eyeclose   #매시안의 침실
    play sound "audio/sfx/bird.ogg"
    play music "audio/music/test.ogg" fadein 0.1
    
    ch_na "-짹짹."

    "잠시 패닉에 빠진 지 얼마나 됐다고 벌써 새가 우는 시간이 됐냐."
    "지금이 몇 시이길래... 앗, 6시 30분인가."
    "한국에서도 이 시간쯤 되면 이른 아침이라 부를 만한 때겠지. "
    "리스는 언제쯤 일어나려나. 그러고 보니 몇 시에 일어나는지를 못 물어봤네."
    "아직 스케줄도 못 짰고 내가 집사란 직책도 잘 모르는 상황이긴 하지만..."
    "그래, 일단 나가보자. 부딪혀보면 알겠지."
    play sound "audio/sfx/door open.ogg"

label chapter1_2_2:
    scene c2-2 with dissolve   #리스의 집(거실)
    ch_na "어우, 햇빛이 거실 창문으로 확 비치네. 여긴 일광욕하기에도 나쁘지 않겠는데?"
    "근데 주위에 리스는 안 보이는구만. 미동도 안 느껴지는 걸 보니 아직 자기 방에서 자고 있겠지."
    "그렇다면..."

    #선택지
    menu:
        "선택지1 : 리스를 깨울까.":  
            play sound "audio/sfx/click button.ogg"
            jump chapter1_2_2_a

        "선택지2 : 아침 식사를 준비할까.": 
            play sound "audio/sfx/click button.ogg"
            ch_na "좋아, 아침밥을 안 먹으면 힘이 나질 않을테니." 
            ch_na "간단하게라도 한 번 차려보자. 요리책에서 눈여겨봤던 게 있기도 하니까." 
            jump chapter1_2_2_b_

label chapter1_2_2_a: #리스를 깨울까
    ch_na "뱀파이어는 평소에 일찍 일어날 것 같은데. 일단 햇빛을 받는 걸 별로 안 좋아하니까."
    "그렇게 생각하면 지금은 늦잠을 자고 있다는 뜻이겠지."
    "리스의 침실이 바로 윗층에 있었지. 어제 청소했을 때 들어가봤으니."
    play sound "audio/sfx/walk.ogg"
    "-탓탓."
    "그래, 문 주위가 꽃과 리본으로 장식된 게 딱 여자가 지내는 방이라고 새겨져 있네."
    "그럼 어디 한 번 노크를..."
    play sound "audio/sfx/knock1.ogg"
    "-똑똑."
    m "주인, 일어날 시간이야."
    play sound "audio/sfx/knock2.ogg"
    "-똑똑똑."

    m "주인?"

    "아무리 노크해도 대답이 없네. 얼마나 푹 자고 있길래..."
    "아직 꿈나라에서 깨어나지 못한 건가."
    play sound "audio/sfx/alarm.ogg"
    "-따르르릉!"
    "어우, 깜짝이야. 한 번 더 노크해보려 시도하던 참이었는데... 미리 알람을 맞추고 잤나 보네." 


    play sound "audio/sfx/door open.ogg"

    scene reese memorial with change007
    image sun bubble = Fixed(SnowBlossom("gui/sun bubble.png", 120, xspeed=(20, 60), yspeed=(50, 400), start=20))
    show sun bubble

    r "으음... 웬 노크소리가 들리는가 혔더니..."
    r "내 깨우려고 왔나?"
    m "어, 어..."

    "눈을 비비며 드러낸 리스의 모습은 어제와는 제법 상반된 분위기였다."
    "고스로리 드레스에서 파자마로 갈아입으니 고고한 귀족에서 앳된 소녀 같은 느낌으로 변했다고 해야 하나."


    r "그... 깨우는 거 땜에 여그로 안 와도 된다카라. 알람이 있으니."
    m "알았어. 기억해둘게."
    r "근디 니도 알람 맞추고 잤나? "
    m "아아, 난 잠이 안 와갖고."
    r "응? 평소에 잠을 설치는 편이가?"
    m "아니, 설쳤다기보다는 자고 싶다는 생각이 전혀 안 들었거든."
    r "에에~ 기런 사람이 어디 있다고..."

    "나도 믿겨지지가 않아. 불침번을 수없이 섰어도 불면증 같은 증상은 없다고 건강검진 때 항상 들었었는데."
    "난 원래 제시간에 잠을 꼬박꼬박 자는 타입이었으니까. 그러니 더욱 아리송할 수밖에."

    jump chapter1_2_2_a_
        
label chapter1_2_2_a_:
    $ persistent.sit[0] = 100 # 기운을 초기화 합니다
    jump My_home2

label chapter1_2_2_c:

    "잠깐의 자유시간을 마치니 주방 쪽에서 리스가 나를 부르는 소리가 들린다"
    m "주방쪽으로 가볼까?"
    scene c1-2 with change020   #주방

    show scg_reese3 normal with dissolve

    
    r "나가 일어나기 전엔 아침부터 만들어 놓으라. 기래야 나가 좀 편해지니."
    r "오늘 어찌 아침을 준비하는 지 잘 봐두그라. 다음 날은 네 몫이다."
    show scg_reese3 walk with fastdissolve
    play sound "audio/sfx/put stuff.ogg"
    pause 0.5
    r "요건 토스트기인기라. 식빵을 바삭하게 구워주는 도구다."
    m "팬에 안 구워도 되는 거야?"
    show scg_reese3 close eyes with fastdissolve
    r "그라니 요 기계를 들인 거지. 편하니께."
    "딱 보니까 기계의 구멍이 토스트만 딱 들어갖게끔 맞춰져 있네." 
    "말 그대로 토스트를 구울 때 쓰는 놈이구만."
    show scg_reese3 normal with fastdissolve
    play sound "audio/sfx/toaster on.ogg"
    "토스트기 안에 빵을 넣고 스위치를 내리자, 째깍거리는 소리가 자그마시 들리기 시작했다."
    r "그리 오래 걸리진 않을 기다. 타이머도 토스트기로 맞춰놨고."
    "오오, 손을 가까이 대보니 열이 굉장한데. 노릇노릇한 냄새도 나는 것 같아."
    "열기를 보니 금방 완성될 것 같은데. 기대되네, 어떻게 나올까."
    play sound "audio/sfx/toaster off.ogg"
    "-띵!"
    show scg_reese3 smile with fastdissolve
    r "꺼내보라. 어떻게 구워졌는지."
    m "오오..."
    "토스트를 안에서 꺼내자, 새하얗던 토스트의 속살이 갈색으로 짙게 물들었다."
    "살살 긁어보니 되게 바삭할 것 같은 느낌도 나고 그래. 것보다 탄자국이 없다는 게 신기할 따름이네."
    show scg_reese3 shake wink smile with fastdissolve
    r "함 맛 봐 보라. 니한테도 맞을 걸."
    play sound "audio/sfx/eating toast.ogg"
    pause 0.8
    "오오, 한 입 물자마자 퍼지는 이 쫀득하면서도 바삭바삭한 식감이라..."
    "나도 아침에 토스트로 해결할까? 먹기에도 간편하지, 맛도 있잖아."
    r "괜찮제?"
    m "응, 이거 되게 맛있다."
    show scg_reese3 smile with fastdissolve
    r "옆에 있는 냉장실에 토스트를 비롯해 아침 재료가 든 층이 있다카라. 거기 있는 재료를 꺼내다 쓰믄 된다."
    m "아침에는 이렇게 있는 걸로만 먹는 거야?"
    show scg_reese3 wink with fastdissolve
    r "와, 집사가 하는 아침은 좀 다른가?"
    m "매번 반복해서 먹는 것 같아가지고."
    r "기런 거로 걱정하기는..."
    "아침에 저런 걸로 계속 먹는 것이 지겹지는 않나 보네."
    "하긴, 아침엔 보통 일정이 있음 빨리 만들고 빨리 먹고 가는 게 낫긴 하지."
    show scg_reese3 close eyes with fastdissolve
    r "원한다믄 굳이 이런 매뉴얼대로 하지 않아도 된다. 단, 맛은 절대 실망시키지 말그라."
    m "알겠어요, 입맛 까다로운 주인 나으리."
    #[흔들리는 연출]
    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=20)
    show scg_reese3 angry with fastdissolve
    r "나가 방금 맛만 실망시키지 말라 기랬지 은제 입맛이 까다롭다 혔냐?"
    r "평타 정도만 치믄 나가 뭐라 안 혀니 억지로 부담 갖지마라.  웬 헛소리를 하는가 혔더니..."
    show scg_reese3 close eyes with fastdissolve
    "그게 입맛이 까다로운 거잖아요, 이 사람아! 본전 맞추기도 얼마나 어려운 일인데!"
    "그 와중에 아침인데도 힘이 되게 팔팔하네. 주먹 맛이 기가 막혀."
    stop music fadeout 3.0
    jump chapter1_2_3

label chapter1_2_2_b_:
    scene c1-2 with dissolve   #주방
    play sound "audio/sfx/fridge open.ogg"
    "-덜그럭..."
    "그게 어디 있었지... 오, 여기 있다!"
    "라벨을 읽어보니 이게 한국에서 주로 먹는 가공육 중에 하나일 거야. 이름은 '유로피언 소시지'라고 적혀있네."
    "고기를 갈아 길쭉한 원통 모양처럼 만든 식품이라, 특이하네. "
    "일단 육류를 이용해 만드니까 어느 정도의 맛은 보장되어 있을 테니 한 번 써봐야지."
    "그 다음은 주식으로 삼을 걸 구해야 하는데... 이거면 될까? "
    "이름은 ‘곡물식빵’, 부제에는 아침 해결사라, 확실한 주식이네."
    "이 정도면 충분하겠어. 제법 괜찮은 접시가 나올 거란 예감이 들어."
    #[화면이 암전됐다가 다시 나오는 연출]
    define eyeclose = Fade(0.5, 0, 1, color="#000000")
    scene c1-2 with eyeclose
    play sound "audio/sfx/plate.ogg"
    "역시 재료랑 조리법이 간단해서 그런지 금방 끝냈다."
    "그냥 굽기만 했는데도 먹음직스러운 비주얼이 나온다는 게 사실이었구나. 요리책으로만 봤을 땐 약간 미신이라 여겼는데."
    show scg_reese3 close eyes with dissolve
    r "으음..."
    m "일어났어?"
    show scg_reese3 wink with fastdissolve
    r "기래. 나가 요때 일어나는 걸 어찌 알았는지는 모르겠다만..." 
    m "늦잠 부릴 것 같지는 않아 보였거든."
    show scg_reese3 silly smile2 with fastdissolve
    r "니 뭐 독심술이라도 부렸나?"
    show scg_reese3 normal with fastdissolve
    "그냥 한 번 해본 소리야. 굳이 따지자면 사람을 많이 만난 경험이라고나 할까."
    "기사단에 지내면서 온갖 다양한 유형의 사람을 봤으니..."
    m "먹어. 다 됐으니까."
    show scg_reese3 shake close eyes with fastdissolve
    play sound "audio/sfx/knife.ogg"
    pause 2.0
    show scg_reese3 wink smile with fastdissolve
    r "호오, 소시지의 육즙이 풍부하구마! 잘 구웠는데?"
    "소시지를 한 입 덥석 베어물었을 때, 펑 터지는 소리와 쫀득쫀득한 식감이 그녀의 입안을 황홀하게 감싸는 것 같았다."
    "빵을 씹을 때도 입가의 미소는 전혀 사그러들지 않고 있네. 이 정도면 아침 식사 가지고 불평 들을 일은 없을 것 같은데?"
    
    #1-1 요리 선택지 여부에 따라 스크립트 달라짐 - 추가
    if Cook_point >= 1:
        r "여그 요리에 벌써 익숙해진 모양이구마. 앞으로 더 기대해도 되겄는걸?"
    else: 
        r "잘 혔네! 슬슬 적응하는 모습이 보기 좋구마."
    
    
    "아침 식사에 관한 결과는 호평이었다."
    "근데 사실 내가 잘했다고 하기에는 그래. 소시지와 빵의 맛이 사전에 어느 정도 보장된 덕분인지라."
    "다음에는 테크닉을 감미해서 만들어보고 싶네. 그럼 더 좋아해 줄지도."
    stop music fadeout 3.0
    $ persistent.sit[0] = 100 # 기운을 초기화 합니다
    jump My_home3


label chapter1_2_3:
    "리스가 주방으로 부른다 따라가 볼까?"
    scene c1-2 with dissolve   #주방
    pause 0.1
    #[화면이 암전됐다가 다시 나오는 연출]
    define eyeclose = Fade(0.5, 0, 1, color="#000000")
    play music "audio/music/castle1.ogg"
    show scg_reese3 normal with dissolve
    r "설거지는 나가 말한 대로 다 마쳤나?"
    m "아까 봤잖아, 삐까번쩍한 거?"
    show scg_reese3 smile with fastdissolve
    r "기래 기래, 대충 봤을 때도 잘 헐 것 같드라."
    "내가 설거지를 얼마나 꼼꼼하게 했는데, 저걸 가지고 퇴짜맞을 이유는 없지."
    "근데 그동안 했던 것 중에서 제일 열심히 한 건데, 그냥 눈흘림으로 끝낸 건 살짝 서운하네."
    "괜히 고생해서... 아니다, 자화자찬으로 만족하면 되지."
    show scg_reese3 angry with fastdissolve
    r "집사."
    m "또 뭔 용건이라도?"
    show scg_reese3 close eyes with fastdissolve
    r "용건이라기보다는 권유에 가까운디..."
    show scg_reese3 normal with fastdissolve
    r "혹시 내 일하는 데에 따라올 마음 있나?"
    "일하는 곳? 여기가 일하는 데 아닌가?"
    "귀족들은 여기서 업무 보고 식사 하고 잠 자고 하루를 대부분 여기서 보낼 텐데."
    "아님 내가 너무 편견에 사로잡혀 있는 걸 지도. 귀족 출신 가수도 존재한 사례가 에르온에서도 있었으니까."
    "가창력은 그럭저럭인데, 돈이 많아서 그런지 성형에 행사에 이것저것 팍팍 쏟아붓더라고."
    "리스도 그런 부류에서 활동하려나."
    show scg_reese3 close eyes with fastdissolve
    r "니 마음대로 혀라. 집에서 나뒹굴고 싶음 기냥 여그에 있고."



    #선택지
    menu:
        "선택지1 : 시내 구경이라도 할 겸...":  
            play sound "audio/sfx/click button.ogg"
            jump chapter1_2_3_a

        "선택지2 : 나 홀로 집에!": 
            play sound "audio/sfx/click button.ogg"
            jump chapter1_2_3_b

label chapter1_2_3_a:

    "주인이 어디서 어떤 걸 하는지는 알아봐야겠지. 그래야 내가 자율적으로 스케쥴을 조정해가며 돕거나 그럴 수 있으니까."

    "세상이 어떻게 돌아가는 지 제대로 구경해봐야 하기도 하고."

    m "동행할게. 여기서 그리 멀지는 않아?"
    r "걸어서 10분이면 된다카라. 따로 준비는 안 혀도 되제?"
    m "챙길 게 있나. 지금 입는 옷만으로도 충분한데."
    r "문제 없음 출발혀자. 기다리고 있는 사람이 있으니."
    stop music fadeout 3.0
    jump chapter1_2_4_a


label chapter1_2_4_a:
    scene black with dissolve
    play sound "audio/sfx/elevator.ogg"
    "-위잉..."
    scene c2-4 with change020
    play music "audio/music/castle2.ogg" fadein 1.0
    show scg_reese3 normal right with dissolve

    r "자, 여그다카라."
    "리스가 일하는 데가 여기구나. 사무공간이 여기저기 붙어있네."
    "입구를 보니 ‘스프링 흥신소’라 적혀 있더만, 의뢰인의 요청을 받고 그에 따른 행동을 하는 곳이려나."
    "내가 예전에 살았던 에르온에 있었을 때는 귀족들이 이런 일을 하지는 않았는데, 여기는 취급이 좀 다른가?"


    show scg_nowell2 walk with lefttoright:
        matrixcolor TintMatrix("#00180d") * SaturationMatrix(0.5)
    mys "여어~ 우리 귀족님 납셨어? 드디어 집사를 구했나 보네?"
    show scg_reese3 close eyes right with fastdissolve
    r  "아직 배울 게 많긴 하지만, 괜찮은 녀석이제."
    show scg_nowell2 shake smile left with fastdissolve:
        matrixcolor TintMatrix("#00180d") * SaturationMatrix(0.5)
    mys "하하핫...! 아직 하루밖에 안 됐잖아."
    mys "사람은 말이야, 뭐 하나 꽂히면 점점 발전하게 되어 있거든."
    mys "먼저 가서 할 일 하고 있어. 집사라는 친구랑 말 좀 터볼 테니까."
    r  "기래."
    show scg_reese3 walk leave right 

    "저 사람이 리스가 고용한 부하직원인가 보네."
    "부하직원이라 하기에는 너무 가벼운 분위기로 리스를 맞이하고 있는데. 지내면서 정이 틀었나 봐?"

    hide scg_nowell2 walk 

    show scg_nowell2 normal left with dissolve


    mys "자, 그쪽도 만나서 반가워!"
    n "난 {color=#00ff04}노웰{/color}이라 해. 우리 버스에서 만난 적 있었잖아?"
    n "그때 내가 운동복 차림에 안경까지 벗었지? 못 알아볼 수도 있겠다."

    "버스에서 운동복 차림이라. 그럼 어제 그때..."


    show scg_nowell sports right with dissolve:
        matrixcolor TintMatrix("#5cffb6") * SaturationMatrix(0.5)


    m "앗! 거기서 내 버스비를 대신 대준 사람이 당신이었군요?"

    hide scg_nowell sports right with dissolve

    m "그땐 정말로 감사했습니다. 당장 갚고 싶지만 월급이 안 들어와서요."
    show scg_nowell2 happy left with fastdissolve
    n "괜찮아! 말 편하게 해도 돼."
    n "월급이 안 들어온 건 아직 계좌를 안 만들었으니 그럴 거야. 오늘 안에 금방 만들어지니 걱정 마."
    n "한국 같은 나라에서는 월급을 계좌로 주는 걸 선호하거든. 현금보다 간편하니까."
    m "한국 같은 나라, 라니...?"
    show scg_nowell2 curious left with fastdissolve
    n "아, 여기는 말이야, 에르온과는 다르게 각 땅을 '나라'라는 형태로 쪼개거든. 한국은 아시아라는 대륙에 있는 작은 땅이야."
    n "원래도 작았지만, 분단이 된 이후로 절반 더 작아졌어."
    m "분단이면 누구한테 땅을 뺏긴 거야?"
    show scg_nowell2 close eyes sad left with fastdissolve
    n "서로 다른 사상을 가진 민족들이 대립해 두 쪽으로 갈라섰는데, 전쟁과 휴전을 거쳐 지금까지 분단 상태로 있어."

    "꽤나 가슴 아픈 사연을 가진 나라구만. 분명 갈라선 사람들 중에 원치 않은 이들도 있을 터인데."
    "근데 가만, 에르온은 어떻게 아는 거야?"
    show scg_nowell2 normal walk middle with dissolve
    n "인사도 치렀으니 하는 일이 뭔지 한 번 소개해줘야겠지?"
    show scg_nowell2 happy with fastdissolve
    n "우린 다양한 사람을 대상으로 의뢰를 받고, 실행하고 있어."
    show scg_nowell2 close smile2 with fastdissolve
    n "그동안 만났던 의뢰인 중에는 회사원도 있고, 아이들도 있고, 마법소녀도 있고... 일일이 세기도 힘드네."
    m "그, 그럼 보통 어떤 의뢰를 받아?"
    show scg_nowell2 normal with fastdissolve
    n "저~기 벽에 붙어 있어. 이번 달 의뢰 목록을 한 번 읽어볼까?"
    show scg_nowell2 smile with fastdissolve
    n "어디 보자, 1일에는 오른팔의 저주 풀어주기, 6일에는 비밀 에이전트 대행, 12일에는 과자 마을 접수..."
    m "그 정도면 괜찮아! 대충 감이 와."
    m "그럼 여기서 역할은 어떻게 돼?"
    show scg_nowell2 close smile2 with fastdissolve
    n "대표인 내가 여기서 의뢰를 접수하고 계획과 일정을 수립한 다음, 실행하는 역할을 하고 있어."
    n "리스는 물품이랑 재정 상태에 관한 조사 및 관리를 담당하고, 중대한 의뢰가 있을 때 돕기도 해."

    "그럼 노웰이 대표고 리스가 조수라 이거네. 사무 공간은 이 둘밖에 없는 것 같던데, 단둘이서 운영하나 봐."
    "근데 리스가 대표가 아니라고 했지. 리스의 오빠라서 그런가? 아님 일처리 능력이 더 좋은 사람인가..."
    "아냐, 아냐. 가만히 생각해 보니 리스가 일을 싫어하는 타입일 수도 있겠다. 일부러 일감 떠넘기려고 대표직을 양보한 걸 수도 있잖아?"

    m "혹시 직원 모집이라도 한 적 있니?"
    show scg_nowell2 curious with fastdissolve
    n "직원은 리스 한 명으로 충분한 걸. 혹시 이쪽 부류에 관심 있어?"
    m "난 집사라 집에 있을 날이 많은데 뭐."
    show scg_nowell2 happy with fastdissolve
    n "에이, 걱정 마! 내가 잘 얘기해갖고 적당한 선에서 부탁하면 되지."
    n  "그리고 걔가 그리 험악한 애는 아니야. 은근 정도 있다고!"

    with Shake((0, 0, 0, 0), 0.2, dist=40)
    "정은 무슨 얼어죽을! 험악하던데! 구속 마법까지 걸었다는 걸 아직 모르나..."

    "-따르르릉!"
    show scg_nowell2 curious with fastdissolve
    n "앗, 업무 전화가 왔네..."
    show scg_nowell2 normal with fastdissolve
    n "밖에서 잠시 통화할 테니 잠깐 쉬고 있어. 배달 오는 데 시간이 좀 걸린다고 했으니까."
    m "배달?"
    show scg_nowell2 smile with fastdissolve
    n "조금 전에 뭘 시켰거든. 있다 같이 먹자! 네 입맛에도 맞을 거야."

    "첫인상은 꽤 괜찮네. 꼼꼼한 면도 있어 보이고."
    "아무리 직원이 한 명이어도 대표직을 맡았다면 책임감이 곧 생명일 터."
    "방금 설립날짜도 봤었는데 16년 전에 했다고 하네. 그 정도면 웬만한 노하우는 다 터득할 경력인데."
    "아무튼 대단하다, 대단해. 반평생을 여기다 바친 사람 아니야."
    jump chapter1_3_1

label chapter1_2_3_b: #나홀로 집에

    "집사로서의 본분을 다하기 위해서는 집에 남아있는 게 옳겠지."
    "감을 봤을 때 내가 여기서 해야 할 일이 아직 남아있을 거야."
    m "혼자 집 관리 잘 하고 있을게."
    show scg_reese3 smile with fastdissolve
    r "하, 아직 온 지도 얼마 안 됐는디 벌써 자신감이 붙었나?"
    m "난 한다면 하지!"
    show scg_reese3 close eyes with fastdissolve
    r "알었다... 발목집을 일만 벌리지 말고."
    show scg_reese3 close eyes middle leave 
    pause 2.5


    "히야~ 드디어 혼자다! 잠깐이지만 이 넓은 데서 자유를 누빌 수가 있게 됐어!"
    "할 일은 살짝만 미뤄두고, 이 행복을 뭘로 시작해볼까? 어마무시한 호가를 자랑하는 술로 해봐?"
    "평소에 낮술은 잘 안 하지만, 이때 아니면 언제 먹어보겠냐."
    "더도 말고 딱 한 모금만 따라서 마셔보자, 시음 수준 정도면 잘 들킬 리 없잖아."
    "-달그락."

    "아으, 깜짝이야! 주방에 웬 인기척이 들리는 거야?"
    "리스가 문 연 사이에 귀신이라도 들어왔나, 아님 환기 때문에 창문을 틀어놨을 때 들어온 바람의 영향인가."

    "어차피 술을 가지러 가야 했던 참이긴 한데 웬지 또 불안스럽네. 오기 전에 환청스런 현상도 겪었지 않았나."

    scene c1-2 with change020
    show scg_nowell2 curious with dissolve:
        matrixcolor TintMatrix("#00180d") * SaturationMatrix(0.5)

    mys "아니, 이건 그토록 구하기 힘든 한정판 위스키 아니야?"
    show scg_nowell2 happy with fastdissolve:
        matrixcolor TintMatrix("#00180d") * SaturationMatrix(0.5)


    mys "어따 숨기고 다녔대냐. 나도 한 번쯤은 맛보고 싶었던 건데!"

    #show c2-1 behind scg_nowell2 with dissolve

    "역시 불길한 예감은 틀리는 법이 없다고 그랬나. 빈집털이범이 왔구만."
    "그래, 저런 놈들을 잡는 것도 집사의 역할이니. 몸이나 풀자고."
    show effect1 video with dissolve
    hide effect1 video with dissolve
    #$ renpy.movie_cutscene("images/effect2.mpg", delay=None, loops=0, stop_music=False) with dissolve

    hide scg_nowell2 happy with fastdissolve
    show scg_nowell2 shake curious left with fastdissolve

    mys "...으앗!!"

    "침입자가 술병에 한눈판 사이, 미동도 느껴지지 않을 정도로 조용히 다가가 양팔로 단숨에 목을 졸라맸다."
    "여기가 적의 아지트었다면 바로 목을 꺾었을 텐데."

    show scg_nowell2 shake curious left with fastdissolve

    mys "자, 잠깐만! 나 너 알거든? 조, 좀만 진정해볼래?"
    m "개소리 마시고요, 조용히 잠들기나 하세요."
    mys "그 버스 있잖아! 너 그때 공항까지 갔었지?"
    m "...뭐?"
    mys "손짓했던 사람이 나야! 버스비도 대신 내줬고!"
    show scg_nowell2 close eyes sad left with fastdissolve
    mys "그때 내가 운동복 차림에 안경까지 벗어 못 알아볼 수도 있겠네..."

    "가만, 그럼 그날 버스에서 봤던 이가 저 사람이었다?"

    show scg_nowell sports right with dissolve:
        matrixcolor TintMatrix("#5cffb6") * SaturationMatrix(0.5)


    "돌이켜 보면 맞는 것 같아. 목소리도 그렇고."
    "헌데 그것하고는 별개로 여긴 무슨 목적으로 들어온 건지는 모르겠지만."
    "일단은 풀어놓고 얘기해볼까."

    hide scg_nowell sports right with dissolve

    show scg_nowell2 shake hurt left with fastdissolve
    mys "켁켁! 아이고, 미리 인사를 했어야 됐는데."
    show scg_nowell2 normal walk middle with dissolve
    n "내 이름은 노웰이야! 리스의 직속 상사지!"
    "직속 상사? 귀족인 리스에게 한 층 더 상관이 존재한다고?"
    m "혹시 어디 쪽에서 일하는데?"
    show scg_nowell2 close smile with fastdissolve
    n "‘스프링 흥신소’라고, 내가 차린 회사가 있어."
    "흥신소라면 의뢰인의 요청을 받고 그에 따른 행동을 하는 곳이려나."
    "내가 예전에 살았던 에르온에 있었을 때는 귀족들이 이런 일을 하지는 않았는데, 여기는 취급이 좀 다른가?"

    show scg_nowell2 curious with fastdissolve
    n "맞다, 리스랑 연봉 협상은 해봤어? 집사로 고용 됐으니 노동에 대한 대가는 받아야 하잖아."
    m "그러고 보니 연봉 협상도 아직 안 했네. 계약서도 안 썼고."
    show scg_nowell2 close smile2 with fastdissolve
    n "리스가 아직 말 안 해줬구나? 아마 계좌 만들면 천천히 답해 줄 거야."
    n "한국 같은 나라에서는 월급을 계좌로 주는 걸 선호하거든. 현금보다 간편하니까."
    m "한국 같은 나라, 라니...?"
    show scg_nowell2 curious with fastdissolve
    n "아, 여기는 말이야, 에르온과는 다르게 각 땅을 '나라'라는 형태로 쪼개거든. 한국은 아시아라는 대륙에 있는 작은 땅이야."
    n "원래도 작았지만, 분단이 된 이후로 절반 더 작아졌어."
    m "분단이라면 누구한테 땅을 뺏긴 거야?"
    show scg_nowell2 close eyes sad with fastdissolve
    n "서로 다른 사상을 가진 민족들이 대립해 두 쪽으로 갈라섰는데, 전쟁과 휴전을 거쳐 지금까지 분단 상태로 있어."

    "으음, 꽤나 가슴 아픈 사연을 가진 나라구만."
    "분명 갈라선 사람들 중에 원치 않은 이들도 있을 터인데."
    "근데 가만, 에르온은 어떻게 아는 거야?"

    show scg_nowell2 normal with fastdissolve
    n "자, 이쯤이면 슬슬 배달 올 때도 됐고 하니..."
    m "잠깐, 이쪽으로 뭐 시킨 게 있다고?"
    show scg_nowell2 close smile2 with fastdissolve
    n "아니아니, 흥신소 쪽에! 마침 가려던 참이긴 한데, 너도 오는 게 좋을 거야!"
    m "응? 나도 가야 한다고?"
    show scg_nowell2 normal with fastdissolve
    n "신분증도 만들어야지, 계좌도 있어야지! 일단 여기서 필요한 건 되도록 오늘 안에 끝내는 게 좋잖아?"

    "쩝, 원래 계획대로라면 이 안을 내 놀자판으로 삼으려 했지만."

    "방금 노웰이 말한 건 밖에서도 놀 수 있을 때 필수품이나 다름 없을 테니까."

    m "그래, 근데 여기서 버스 타고 가?"
    show scg_nowell2 close smile with fastdissolve
    n "걸어서 얼마 안 걸려! 여기 근처거든."
    m "그럼 주인이 지각할 걱정은 없겠구만?"
    show scg_nowell2 smile with fastdissolve
    n "애초에 걔는 집을 이곳으로 정했으니까."
    stop music fadeout 3.0
    jump chapter1_2_4_b

label chapter1_2_4_b:
    scene black with dissolve
    play sound "audio/sfx/elevator.ogg"
    "-위잉..."
    scene c2-4 with change020
    play music "audio/music/castle2.ogg" fadein 1.0

    show scg_nowell2 normal left with fastdissolve
    n "리스! 나 왔어!"
    show scg_reese3 angry walk with righttoleft
    r "마, 또 지각이가? 요새 아주 밥 묵듯이 혀네?"
    show scg_nowell2 smile left with fastdissolve
    n "니네 집사 좀 데리려고 왔어. 아직 연봉 협상도 안 했다며?"
    show scg_reese3 silly smile2 right with fastdissolve
    r "연봉...? 아아, 깜빡혔구마."
    show scg_reese3 normal right with fastdissolve
    r "근디 분명 집에 있다 혔는디. 금새 맘이 바꼈나?"
    m "이런 저런 사정 때문에..."
    show scg_nowell2 close smile left with fastdissolve
    n "차피 여기 땅에 들어왔을 때부터 필요했던 거잖아. 아직 혼자서 뭘 어찌 해보겠어."
    show scg_reese3 angry right with fastdissolve
    r "넘 과소평가마라. 다 큰 놈헌테 어린애 취급하기는."
    show scg_nowell2 smile left with fastdissolve
    n "너도 아직 어린 걸 뭐, 성인 딱지만 뗐지. 작년까지 누가 리스 집을 관리했는지는 알고?"

    play sound "audio/sfx/smash.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=20)

    show scg_nowell2 shake hurt left with fastdissolve

    n "아야얏! 아까 목도 졸렸는데..."
    show scg_reese3 close eyes right with fastdissolve
    r "기럼 오늘 더 맞아야 쓰것네. 기래야 머리가 말짱해지지."

    "상관인 노웰도 리스 앞에서는 주먹 한 방에 두 손을 번쩍 드네. 제일 어린 놈이 제일 매섭다 이건가."

    show scg_nowell2 close smile left with fastdissolve
    n "이, 일단 인사도 치렀으니 하는 일이 뭔지 한 번 소개해줘야겠지?"
    show scg_nowell2 normal left with fastdissolve
    n "우린 다양한 사람을 대상으로 의뢰를 받고, 실행하고 있어."
    show scg_reese3 wink right with fastdissolve
    r "그동안 만났던 의뢰인 중에는 회사원도 있고, 애들도 있고, 마법소녀도 있고... 일일이 세기도 힘들구마."
    m "그, 그럼 보통 어떤 의뢰를 받아?"
    show scg_nowell2 normal left with fastdissolve
    n "저~기 벽에 붙어 있어. 이번 달 의뢰 목록을 한 번 읽어볼까?"
    show scg_nowell2 smile left with fastdissolve
    n "어디 보자, 1일에는 오른팔의 저주 풀어주기, 6일에는 비밀 에이전트 대행, 12일에는 과자 마을 접수하기..."
    show scg_reese3 close eyes right with fastdissolve
    r "그 정도면 됐다카라. 대충 감이 올 기다."
    m "그럼 여기서 역할은 어떻게 돼?"
    show scg_nowell2 close smile left with fastdissolve
    n "대표인 내가 여기서 의뢰를 접수하고 계획과 일정을 수립한 다음, 실행하는 역할을 하고 있어."
    n "물품이랑 재정 상태에 관한 조사 및 관리를 담당하고, 중대한 의뢰가 있을 때 돕기도 해."

    "그럼 노웰이 대표고 리스가 조수라 이거네. 사무 공간은 이 둘밖에 없는 것 같던데, 단둘이서 운영하나 봐."
    "근데 리스가 대표가 아니라고 했지. 리스의 오빠라서 그런가? 아님 일처리 능력이 더 좋은 사람인가..."
    "아냐, 아냐. 가만히 생각해 보니 리스가 일을 싫어하는 타입일 수도 있겠다. 일부러 일감 떠넘기려고 대표직을 양보한 걸 수도 있잖아?"

    m "혹시 직원 모집이라도 한 적 있니?"
    show scg_reese3 normal right with fastdissolve
    show scg_nowell2 curious left with fastdissolve
    n "직원은 리스 한 명으로 충분한 걸. 혹시 이쪽 부류에 관심 있어?"
    m "난 집사라 집에 있을 날이 많은데 뭐."
    show scg_nowell2 happy left with fastdissolve
    n "에이, 걱정 마! 내가 잘 얘기해갖고 적당한 선에서 부탁하면 되지."
    show scg_nowell2 close smile left with fastdissolve
    n "리스 쉬는 날에 한 번 놀러 와서 같이 한탕 뛰자고 하면 흔쾌히 동의해줄 거야!"
    show scg_reese3 angry right with fastdissolve
    r  "최종 권한은 내한테 있으니 조용혀라! 얘가 니 주인이가?"
    show scg_nowell2 smile left with fastdissolve
    n  "어이구, 험상궂으셔라~"


    "-따르르릉!"

    show scg_nowell2 curious with fastdissolve
    n "앗, 업무 전화가 왔네..."
    show scg_nowell2 smile with fastdissolve
    n "밖에서 잠시 통화할 테니 잠깐 쉬고 있어."
    show scg_reese3 normal right with fastdissolve
    n "그리고 방금 배달 시킨 데서 시간이 좀 걸린다고 메시지가 왔거든?"
    n "저쪽에 간식 바구니가 있으니까 배고프면 먹어. 비싼 과자도 사이에 숨겨져 있으니까."
    show scg_nowell2 smile walk left leave 
    pause 2.0
    show scg_reese3 walk right to middle 

    r "어이, 집사."
    m "왜?"
    r "혹시 노웰이 고성에서 뭔 짓이라도 벌였나?"
    m "한정판 위스키를 마시려는 듯 했어."
    show scg_reese3 silly smile2 with fastdissolve
    r "자, 잠깐. 기럼 따부렸나?"
    m "그 전에 저지했지. 건드리면 큰일날 거라는 걸 아니까."
    show scg_reese3 close eyes  with fastdissolve
    r "후우... 보안 방식을 바꿔도 금방 뚫고 난리구마. 꼭 나가 있을 때만 오라고 신신당부혔는디."
    show scg_reese3 angry with fastdissolve
    r "금세 또 기런 걸 노려? 내보다도 철이 덜 든 자슥 같으니."

    "방금 만난 노웰도 리스처럼 보통은 아닌가 봐. 귀족을 부하직원으로 둘 정도면."
    "리스네 거처도 제맘대로 들어오는 걸 보면 뭔 능력을 가지고 있는 것 같아."
    "설립날짜를 봤을 때 16년 전에 열었다고 했었지. 그 정도면 웬만한 노하우는 다 터득할 경력이니까."

    scene black with eyecloseslow
    "챕터3 - 저는 간첩이 아닙니다"

    jump chapter1_3_1

#[챕터 1-3]

label chapter1_3_1:


    scene c2-4 with change020
 
    play music "audio/music/castle2.ogg" fadein 1.0 
    show scg_nowell2 close eyes sad middlein 
    n "후아... "
    m "뭔 협박 전화라도 받았니? 얼굴이 영 시원찮은데."
    show scg_nowell2 shake curious middle with fastdissolve
    n "에이, 그랬다면 바로 집까지 확... "
    # show c3-3 behind scg_nowell2 with dissolve
    m "쫓아가서 응징하겠다 이거구나. 좋은 마음가짐이야."
    show scg_nowell2 smile with fastdissolve
    n "흐흐흐, 경찰 부르는 것보단 속 시원하잖아."
    show scg_nowell2 close smile with fastdissolve
    n "어쨌든, 의뢰와 관련된 거였어."
    n "원래 그런 전화에는 이것저것 막 생각하게 되거든. 어느 장소에서 어떤 방식으로 일처리를 하냐..."

    "꽤 어려운 의뢰를 받은 모양이네. 그런 일엔 머리를 빡세게 굴려 좋은 플랜을 만들어야 수월할 테니까."

    m "계획은 보통 네가 짜?"
    show scg_nowell2 normal with fastdissolve
    n "그렇지. 리스가 머리 나빠서 하는 소리는 아니지만..."
    n "내가 별난 일들을 걔보다 훨씬 많이 겪었으니까. 어떻게 돌아가는지는 대충 감이 오거든."
    m "그렇구나."
    m "근데 배달 시킨 건 언제 온대?"
    show scg_nowell2 close smile with fastdissolve
    n "지금 오고 있대. 얼마 안 있음 올 거야."
    n "그때까지 신분증 문제부터 해결하자고! 여기서 금방 만들거든."
    m "신분증을 네가 만든다고?" 
    show scg_nowell2 smile with fastdissolve
    n "그런 시스템이 우리 흥신소에서는 다 있답니다~?"

    "그런 일은 보통 행정기관에서 하지 않나. 한때 공무원으로 일한 경험이 있나 봐?"
    show scg_nowell2 normal with fastdissolve
    n "저쪽 방으로 들어가자. 신분증을 만들기 위한 사진부터 찍어야 하니까."

    show scg_nowell2 normal walk middle leave
    pause 2.0

    scene c2-4 with change007   # 스프링 흥신소 : 노웰의 방

    show scg_nowell2 hurt with dissolve
    n "아으, 안 꺼낸 지 얼마 됐다고 카메라에 먼지가 쌓여?"
    m "어떻게 나와도 상관은 없는데."
    show scg_nowell2 shake curious middle with fastdissolve
    n "에이, 신분증은 자기의 또다른 얼굴이나 마찬가지야. 대충 찍으면 안 돼."
    show scg_nowell2 close eyes sad with fastdissolve
    "아냐, 그냥 아무렇게나 찍어 줘! 이딴 빌어먹을 얼굴에 공들일 필요가 있겠어?"
    "이럴 줄 알았음 원래 피부색으로 돌아올 수 있는 화장법이나 알아올 걸 그랬나."
    show scg_nowell2 normal with fastdissolve
    n "오케이! 먼지도 다 털었고, 작동 이상도 없고!"
    n "미소 환하게 짓고! 하나, 둘, 셋!"
    
    scene c2-4 with eclipsy3
    play sound "audio/sfx/camera.ogg"
    show scg_nowell2 normal with dissolve
    n "어때, 잘 나왔지?"
    m "깔끔하게 나왔네." 
    "사진을 보니 다시 봐도 이질적이야. 아직도 이게 내 진짜 얼굴인지 익숙치가 않다니까."
    "여기서도 보정 프로그램 같은 걸 써서 피부색만 어떻게 해줄 수 있으려나."
    "...됐다. 그럼 완전 다른 사람 같아 보일 것 같으니까. 신분증은 자기의 또다른 얼굴이라며."
    show scg_nowell2 close smile2 with fastdissolve
    n "오케이! 사진은 이걸로 해주면 되겠고."
    n "여기 종이에다 이름도 적어줘. 그래야 신분증이 만들어지니까."
    show scg_nowell2 normal with fastdissolve
    n "아, 물론 원래 이름 대신 다른 걸로 개명해도 돼. 한국에서 쓰는 이름 방식이 에르온하고 다르니까."

    jump chapter1_3_1_a

label chapter1_3_1_a:
    hide scg_nowell2 normal with dissolve
    # 이후 매시안의 이름이 플레이어의 이름에 의해 바뀜 (m 대신 my로 표기)
    $ povname = renpy.input("이름을 적어주세요.", length=40)
    my "여기."

    if povname == "매시안":
        show scg_nowell2 normal with dissolve
        n "이름이 [povname](이)라... 똑같네!"
    #이름이 없을 때
    elif povname == "":
        show scg_nowell2 curious with dissolve
        n "앗, 이름이 없는데? 깜빡하고 못 쓴 거야?"
        show scg_nowell2 normal with dissolve
        n "그렇다면 다시 종이를 줄테니 적어서 줘!"
        call chapter1_3_1_a

    elif povname == "노웰":
        show scg_nowell2 normal with dissolve
        n "이름이 [povname](이)라... 내 이름을 썼네!"
    elif povname == "리스":
        show scg_nowell2 normal with dissolve
        n "이름이 [povname](이)라... 리스의 대타라도 뛰려고 그래?"

    elif povname == "스칼라":
        show scg_nowell2 normal with dissolve
        n "이름이 [povname](이)라... 혹시 미래에서 온 건 아니지?"
    else:
        show scg_nowell2 normal with dissolve
        n "이름이 [povname](이)라... 오케이!"
    n "잘못 썼으면 다시 쓸래?"

    
    menu:
        "선택지1 : 다시 쓸게.":  
            n "그럼 다시 종이를 줄게. 거기다 적어서 줘!"
            call chapter1_3_1_a

        "선택지2 : 이대로 만들어줘.":
            jump chapter1_3_1_b

label chapter1_3_1_b:
    show scg_nowell2 smile with dissolve
    n "그럼 이걸로 만들어줄게! 조금만 기다려봐~"
    stop music fadeout 2.0
    
    #화면 암전 후 다시 뜸
    scene black with dissolve
    scene black with dissolve
    scene c2-4 with dissolve 

    play music "audio/music/castle2.ogg" fadein 1.0 
    show scg_nowell2 normal walk middle with fastdissolve
    n "다 됐다! 한 번 봐봐!"
    my "'주민등록증'이라... 사진은 잘 보이고, 여기에 붙은 숫자들은 뭐야?"
    show scg_nowell2 smile with dissolve
    n "'주민등록번호'라고, 너도 이제 한국 사람이라는 걸 증명할 수 있는 번호야!"
    my "아아, 그래?"
    "아직 2일차 밖에 안 됐는데 벌써 여기 나라 사람이라는 소리를 듣다니."
    "너무 어색하기 그지없지만 어쩌겠어. 당분간 여기서 죽치고 살아야 하는데, 뭐."
    play sound "audio/sfx/elevator 2.ogg"
    del "배달이요~!"
    show scg_nowell2 shake curious middle with fastdissolve
    n "네에, 잠시만요~"
    show scg_nowell2 normal with fastdissolve
    n  "타이밍 맞춰서 왔네, 받으러 가자!"

    scene c2-4 with dissolve   #장소3 - 스프링 흥신소
    del "맛있게 드세요."
    n "감사합니다!"
    my "그릇을 보니 전부 면요리네. 한 쪽은 매콤한 국물에 해물이 들어가 있고, 다른 한 쪽은 검은 소스가 부어져 있구만."
    my"근데, 인사만 하고 간다고? 돈은 안 내고 가도 되나?"
    show scg_reese3 walk left to right with fastdissolve
    r "핸드폰 앱으로 결제를 미리 혔다카라. 그람믄 직접 돈 낼 필요가 없제."
    "아, 그래서 배달원한테 돈을 안 내도 되는 거였구나."
    "내가 살던 에르온에서는 이런 시스템이 없었는데, 편해 보이네."
    show scg_nowell2 normal walk right to left with fastdissolve
    n "자, 얼른 불기 전에 먹어볼까?"
    n "둘 중 마음에 드는 걸로 하나 골라봐! 나머지 하나는 내가 먹을게!"

        #선택지
    menu:
        "선택지1 : 매콤한 국물이 담긴 면":  
            jump chapter1_3_a

        "선택지2 : 검은 소스가 담긴 면":
            jump chapter1_3_b

label chapter1_3_a: # 매콤한 국물

    
    "갑자기 매운 게 땡기기도 하고, 익숙한 느낌이 드는 음식이기도 하니."
    my "갑자기 매운 게 땡기기도 하니 이걸 먹을게."
    show scg_nowell2 shake smile left with fastdissolve
    n "으흠~ 매콤한 게 땡겼나 보구나?"
    show scg_nowell2 close smile2 left with fastdissolve
    n "요건 면을 먼저 먹고, 이어서 해물을 집어 먹으면 돼. 국물도 들이켜서 마시면 좋고."
    "겉으로 보기엔 적당하게 매울 것 같아 보이는데, 어디 한 번..."
    play sound "audio/sfx/noodle.ogg"
    pause 2.0
    play sound "audio/sfx/silly.ogg"
    with vpunch
    my "켁켁!"
    show scg_nowell2 curious left with fastdissolve
    show scg_reese3 silly smile right with fastdissolve
    r "괜찮나? 물이라도 따라줘?"
    my "응... 고춧가루가 목에 걸렸는지 엄청 따갑더라."
    show scg_reese3 normal right with fastdissolve
    n "부담스러우면 이걸 먹을래? 아직 입에 안 댄 건데."
    my "아냐, 원래 매운 거 먹으면 이런 일이 있거든. 맛은 있으니 걱정 마."
    show scg_nowell2 close eyes sad left with fastdissolve
    n "이럴 줄 알았음 맵기 강도를 더 약하게 할 걸 그랬나..."
    my "몇 단계로 했는데?"
    show scg_nowell2 normal left with fastdissolve
    n "총 4단계 중에 3단계. 보통 것보다 쎈 편에 속하지."
    show scg_nowell2 close smile left with fastdissolve
    n "내가 원래 매운 걸 좋아해갖고 그걸 자주 먹는데, 하핫..."
    "이게 3단계짜리라... "
    "근데 예상보다는 그리 맵지가 않았다. 매운 거 먹는 데는 일가견이 있으니까."
    "이 정도면 4단계도 먹어볼 만 하겠고, 난 오히려 재료 곳곳에 불향이 잘 배여서 마음에 드는데? "
    my "이 음식은 뭐라고 불러?" 
    show scg_reese3 shake close eyes right with fastdissolve
    r "'짬뽕'이라 현다. 중화요리의 대표 마스코트제. 검은 소스가 담긴 그릇은 '짜장면'이라 카고."
    my "그렇구나... 중화요리라."
    "중화요리란 것도 여기 세계의 음식 스타일 중 하나겠지? 나중에 이쪽 요리도 한 번 도전해볼만 하겠는데."
    jump chapter1_3_2


label chapter1_3_b: # 검은 소스

    "저 검은 소스가 부어진 면이 어떤 맛일지 흥미로워 보이는데."
    "그래, 저걸로 가보자. 한 번 먹어봐야 궁금증이 풀리겠어."
    my "이걸 먹을게."
    show scg_nowell2 shake smile left with fastdissolve
    n "요걸로? 알겠어."
    show scg_nowell2 close smile2 left with fastdissolve
    n "위에 올라가져 있는 게 '춘장'이라고 하는 소스인데, 그걸 면하고 비벼서 먹으면 돼."
    play sound "audio/sfx/noodle.ogg"
    pause 2.0
    my "으으으음...!"
    "부드러운 면에서 느껴지는 달달하고 짭짤한 춘장이 예술인데?"
    "거기에 고소하고 기름진 고기와 야채들이 조화를 이루어 내 입안을 즐겁게 하고 있어."
    show scg_nowell2 close smile left with fastdissolve
    r "나쁘지 않제?  출출할 때 이걸 먹으면 기가 막히거든."
    my "하하... 그럴 것 같더라. 근데 이걸 뭐라고 불러?"
    show scg_reese3 shake close eyes right with fastdissolve
    r "요건 짜장면이라 현다. 중화요리의 대표 마스코트제. 매콤한 국물이 담긴 그릇은 '짬뽕'이라 혀고."
    my "그렇구나... 중화요리라."
    "중화요리란 것도 여기 세계의 음식 스타일 중 하나겠지? 나중에 이쪽 요리도 한 번 도전해볼만 하겠는데."
    jump chapter1_3_2


label chapter1_3_2: 
    #화면 암전 후 다시 뜸
    scene black with dissolve
    scene black with dissolve
    scene c2-4 with dissolve #흥신소
     
    my "후아..."
    show scg_nowell2 close smile left with fastdissolve
    n "잘 먹었다아~"
    "만족스러운 한 끼였어. 한국에 와서 처음으로 제대로 먹어본 음식이라 그럴 진 모르겠지만."
    "앞으로 요런 음식을 자주 접하게 될 테니 좋은 경험이라 생각해야지."
    my "원래 이렇게 자주 시켜먹는 편이야? "
    show scg_nowell2 normal left with fastdissolve
    n "내부에 요리할 때가 없으니 그럴 수밖에. "
    show scg_reese3 normal right with fastdissolve
    n "그리고 바쁜 일이 있음 식사는 후딱 해치우는 게 좋잖아. 그럴 때 면요리가 제격이지."
    r "요게 원래 금방 거덜 나는 음식이다. 시간이 지남 뿔어갖고 맛이 안 좋아지기도 혀고."
    "두 사람의 말 모두 일리가 있다. 젓가락 몇 번 들었다 놨다 하면 한 그릇 뚝딱 해치울 수 있으니까."
    "에르온에서도 빨리 먹고 일자리로 돌아가야 하는 사람들이 선호하는 게 면요리니까."
    show scg_nowell2 shake hurt left with fastdissolve
    n "으으~ 밥을 먹으니 바람이 쐬고 싶어졌어."
    show scg_nowell2 close smile2 left with fastdissolve
    n "리스는 여기 있을래?"
    show scg_reese3 close eyes right with fastdissolve
    r "내는 좀 피곤해가지고... 잠깐 소파에 누워야 쓰것다."
    n "그럼 잠깐 쉬고 있고, 우린 디저트를 사러 가자! 근처에 죽이는 스위츠 가게가 있어."
    my "어떤 디저트?"
    show scg_nowell2 smile left with fastdissolve
    n "두말하기에는 인기 상품이 너무 많거든. 따라와보면 알 거야."
    show scg_nowell2 smile walk left leave with fastdissolve
    hide scg_reese3 close eyes right with dissolve
    pause 2.0
    stop music fadeout 2.0
    jump chapter1_3_3
    
    
    
label chapter1_3_3:
    scene c3-4 with change007
    play music "audio/music/busan.ogg" fadein 1.0 
    show scg_nowell2 normal walk right to middle with fastdissolve
    n "동네 탐방은 이번이 처음인가?"
    my "처음에 왔을 때 시장을 한 번 구경해봤어. 말은 잘 안 통했지만..."
    show scg_nowell2 close smile with fastdissolve
    n "맞다, 맞다! 거기서 버스를 탔었지?"
    n "버스 정류장이 있는 건 어케 알았어?"
    my "몸을 이리저리 휘저어서..."
    show scg_nowell2 smile  with fastdissolve
    n "하핫... 하긴, 처음에는 그리 될 수 밖에 없겠지."
    n "이젠 리스 덕분에 말도 잘 틀게 됐잖아. 속이 뻥 뚫리지 않아?"
    my "뚫리기는! 아직 답답한 게 산더미거든?"
    show scg_nowell2 close smile2 with fastdissolve
    n "그래, 그래! 원래 네가 살던 곳이 아니잖아."
    n "적응하다 보면 원래 세계와 거의 다를 바가 없어. 금방 현지인과 다름없다니까?"


    jump chapter1_3_4

label chapter1_3_4:
    scene c3-5 with change007

    n "자! 저기 왼쪽에 고풍스런 인테리어를 한 쪽이 내가 말했던 곳이야."
    n "완전 쩔지? 여기 시내의 대표 마스코트거든!"
    "노웰이 가리킨 스위츠 가게는 다른 건물하고는 다르게 이색적인 외관을 갖추고 있었다."
    "곳곳에 창문도 수두룩하고, 인테리어도 고급지네. 시내 가게 중에 독보적인 것 같아."
    show scg_nowell2 smile with fastdissolve
    n "여기는 디저트를 파는 시간이 점심과 저녁으로 정해져 있어."
    n "예전에는 디저트를 사기 위한 줄이 밖에서 수두룩했는데, 지금은 점심 한정으로 예약제로 바뀐 상태야."
    my "얼마나 많았길래 예약제까지 걸었대. 그 정도로 명물인 건가."
    hide scg_nowell2 smile with dissolve
    stop music fadeout 2.0
    play sound "audio/sfx/crowd.ogg"
    "음? 갑자기 뒤에서 사람들이 술렁거리는 소리가 들리는데."
    "여기에 인지도가 최고라 불리는 연예인이라도 왔나."
    scene c3-4 with change007
    #스칼라 명칭 scala -> s로 수정
    show scg_scala2 angry leftin with dissolve:
        matrixcolor TintMatrix("#1f1e1e") * SaturationMatrix(0.5)  
    play music "audio/music/warning.ogg" fadein 1.0
    mys "흐으으으..."
    n "저것 봐. 우릴 죽일 듯이 노려보고 있네. 쟤가 그 여자인 것 같아."
    my "어딘가 정신이 어긋나 보이기도 한 걸 보면 정상으로 보이진 않는데..."
    my "근데 아는 사이야?"
    n "리스가 최근에 저 애를 본 적이 있었대. 이름은 '스칼라', 한때 리스의 친구였지."
    my "친구? 그럼 당장 가서 구해 줘야지! "
    n "그러면 좋겠지만... 네가 생각하는 그런 방법으론 힘들 거야."
    n "지금 저 애가 리스를 죽이고 싶어 안달이 났다 그러거든."
    show scg_scala2 angry left with dissolve:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)  
    s "피냄새, 리스 거..."
    n "역시 리스의 흔적을 맡고 온 건가. 아님 우리 체취를 맡은 거일 수도 있겠네."
    n "저 애는 내가 손 봐줄게. 물러나 있어."
    my "잠깐, 나도 싸울 수 있는데?"
    n "괜찮아, 혼자서도 충분하고도 남아."
    n "돕고 싶은 마음은 이해하지만 그 과정에서 네가 다치는 모습을 보기는 싫어."
    n "주변 사람들이 휘말리지 않게끔 공간을 벌려줘, 알겠지?"
    my " ...알았어."
    "주변 분위기도 심상치 않은 것 같으니 그의 말대로 해야겠다. 지켜보면서 상황 파악이나 해야지."
    show scg_scala2 smile2 left with fastdissolve
    s "리스, 있는 곳, 당장 말해...!"
    show scg_nowell2 normal rightin with fastdissolve
    n "그 도끼만 치우면 순순히 응해줄게."
    show scg_scala2 shake angry left with fastdissolve
    s "거짓말..."
    show scg_nowell2 curious right with fastdissolve
    stop music fadeout 2.0
    n "오오, 바로 눈치채네? 그냥 한 번 해본 말인 걸 어떻게 간파해댔냐."
    show scg_nowell2 smile right with fastdissolve
    show c3-4 with dissolve:
        matrixcolor TintMatrix("#e0ffdf") * SaturationMatrix(0.5)  

    play sound "audio/sfx/magic barrier.ogg"
    "노웰이 양손으로 바닥을 찍어 거대한 마법진을 펼치자, 장벽이 솟아나 둘을 감쌌다."
    play music "audio/music/scala battle.ogg" fadein 1.0
    "장벽이 스칼라와 노웰만 둘러싼 걸 보면 왜 공간을 벌려놓으라 한 건지 알겠네. 인명피해를 최소화시키려 그러는 거겠지."

    show scg_nowell2 curious right with fastdissolve
    n "자, 들어와봐. 성형 비용은 안 대줄 거다?"
    show scg_scala2 smile2 left with fastdissolve
    s "닥쳐...!"
    play sound "audio/sfx/hit.ogg"
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "서로를 가둔 장벽 안에서, 서로의 공격이 굉음을 내질렀다."
    "움직임이 둘 다 재빠르고 날카로워. 일반인이 보면 어떤 일이 벌어지는지 가늠하기 힘들겠는데." 
    show scg_nowell2 close smile2 right with fastdissolve
    n "이야, 제법 하는데! 요런 몸놀림은 어디서 배웠어?"
    show scg_scala2 shake angry left with fastdissolve
    s "입 다물라 했지...!"
    show scg_scala2 angry left to right2 with fastdissolve
    play sound "audio/sfx/hit 2.ogg"
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "보니까 스칼라의 공격이 정말 거침없구만. 오로지 빈틈만을 찾아 도끼를 휘두르고 있어."
    show scg_nowell2 smile right with fastdissolve
    n "아가씨, 계속 그렇게 쉴 새 없이 날뛰시면 금방 지치실 텐데요?"
    "그걸 일일이 전부 막아내는 노웰도 만만찮아. 접근하기만 하면 마법으로 충격을 가해 거리를 벌리고 있어."
    "끊임없는 맹공을 침착하게, 그것도 가벼운 상처란 것도 없이 능숙히 막아내네. 산전수전 별 일을 다 겪은 경험 덕분이라 봐야 하나."
    show scg_scala2 shake angry left with fastdissolve
    s "후우, 후우..."
    show scg_nowell2 curious right with fastdissolve 
    n "그러게 내가 금방 말했잖아. 그렇게 싸우면 체력 소모가 엄청나."
    show scg_scala2 smile left with fastdissolve
    s "으으으으...!!"
    n "계속 그리 달려드시겠다? 근성이 참 대단해요."
    show scg_nowell2 normal right with fastdissolve
    n "좋아, 사정거리에 들어왔으니 나도 힘껏...!"
    play sound "audio/sfx/magic hit.ogg"
    show push video with dissolve
    hide push video with dissolve
    pause 0.1
    play sound "audio/sfx/wall push.ogg" volume 0.5
    show scg_scala2 smile2 leftout with fastdissolve
    with Shake((0, 0, 0, 0), 0.8, dist=30)
    n "아이고, 벽 부딪히는 게 예사롭지 않은데. 등골이 뻐근하겠어."
    show scg_nowell2 smile right with fastdissolve
    n "야구장이었으면 분명 홈런도 노려봤을텐데, 아쉽구만."
    stop music fadeout 1.0
    play sound "audio/sfx/portal.ogg"
    show portal open video with dissolve
    pause 2.0
    hide portal open video with dissolve
    play music "audio/music/in the soul.ogg" fadein 1.0
    show scg_nowell2 curious right with fastdissolve 
    "노웰이 마무리를 지으려고 할 때, 갑자기 커다란 구멍이 기운을 내뿜으며 등장했다."
    n "잠만, 저건 에르온에서 지역을 넘나들 때 사용하던 포탈이잖아. 도망가려는 건가?"
    show scg_scala2 smile2 leftin with fastdissolve
    s "전부 다..."
    
    show scg_scala2 shake angry left with fastdissolve
    with Shake((0, 0, 0, 0), 0.2, dist=30)
    s "{size=+18}{color=#eaa6ff}지옥으로 가버려!!{/color}"

    play sound "audio/sfx/portal crash.ogg" volume 1.8
    hide scg_scala2 small angry left with fastdissolve
    hide scg_nowell2 smile right with fastdissolve
    with Shake((0, 0, 0, 0), 0.4, dist=30)
    "이런, 갑자기 포탈에 엄청난 인력이 붙기 시작했어!"
    "일단 노웰이 포탈과 자신 사이에 결계를 쳐놓은 덕분에 끌릴 걱정은 보이지 않아 다행이지만."
    
    show scg_nowell2 curious right with fastdissolve
    n "칫, 어째 에르온 포탈에 저런 기술을 넣어놨대? 저런 건 들어본 적도 없는데."
    my "노웰!"
    n "그래, 거기 상황은 괜찮아?"
    m "그렇긴 한데, 네가 안 괜찮을 것 같은데? 멈출 수 있는 방법은 있어?"
    show scg_nowell2 close eyes sad right with fastdissolve
    n "저런 현상을 보는 건 나도 처음인지라... 보통 포탈은 일정 시간이 지나면 자동으로 닫히거든."
    n "안 그러면 안으로 직접 들어가서 포탈 가동을 중단 후 리셋해서 다시 돌아오든가 해야 할 걸."
    my "그럼 내가 직접 가서 멈추고 다시 돌아올게. 해줄 수 있겠어?"
    show scg_nowell2 curious right with fastdissolve
    n "아냐! 그건 너무 위험해!"
    n "안에서 그 소녀와 마주할텐데. 잘못하면 여기에 못 돌아올 수도 있어! "
    my "그 애한테 당할 거란 생각은 전혀 안 해도 돼. 저런 비슷한 건만 수없이 겪었다고."
    show scg_nowell2 close eyes sad right with fastdissolve
    n "평소 했던 거랑 저거랑 같냐...?"
    my "한 번만 믿어줘. 못 돌아오게 되면 그땐 네 말을 전적으로 따를게."
    show scg_nowell2 hurt right with fastdissolve
    n "...하아."
    n "너도 어떻게 보면 리스랑 다를 바가 없네."
    show scg_nowell2 close eyes sad right with fastdissolve
    n "무기 필요하지 않아? 주먹을 전문으로 하는 사람 같지는 않아 보이던데."
    my "아, 그럼 가벼운 한손검으로..."
    play sound "audio/sfx/give sword.ogg"
    show c3-4 with eclipsy5
    show scg_nowell2 curious right with fastdissolve
    n "그래, 이거면 되지? 휘두르기에도 적당한 녀석으로 맞춰줬어."
    my "고맙다."
    n "마력으로 만든 거라 하루 정도 지나면 사라지니 명심해."
    show scg_nowell2 close eyes sad right with fastdissolve
    n "아까도 말했지만 네가 다치는 모습을 보기는 싫다고 했어. 그럼 정말 혼나?!"
    my "분부대로!"
    show scg_nowell2 normal right with fastdissolve
    n "그럼 셋 셀게. "
    n "셋, 둘... 하나!"
    stop music fadeout 2.0
    play sound "audio/sfx/portal in.ogg"
    jump chapter1_4


    

