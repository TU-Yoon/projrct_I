define my = Character('fl', color="#00ff04")

#[챕터 1-4 다시 만난 세계]
label chapter1_4:
    scene black with slowflash
    "챕터 EX - 다시 만나버린 세계"
    #[장소1 – 리저렉션 라이프 랩 – 제5포탈룸]
    play sound "audio/sfx/portal out.ogg"
    scene c4-1 with slowflash2
    play music "audio/music/science 1.ogg" fadein 2.0

    "후아... 정말 아찔하네."

    "정신줄 붙들어매지 않았으면 기절한 채로 공간을 이동했겠지. 지금 인력이 약해진 상태라 다행인가."
    play sound "audio/sfx/shutdown.ogg" fadein 2.0
    pause 1.0
    "일단 포탈 제어 장치의 전원을 꺼 가동이 멈췄다. 그럼 반대편에서도 상황은 진정됐겠지."
    "이제 어떻게 다시 돌아올지 생각해야 해. 이 근방에서 방법을 아는 사람이 있으려나."
    play sound "audio/sfx/lab door open.ogg" volume 1.5
    #[장소2 – 리저렉션 라이프 랩 – 2층 복도]
    scene c4-2 with change007
    "확실히 이런 사고에는 인명피해도 절대 무시할 수 없는 법이다."
    "피로 얼룩진 채 널부러져 있는 연구원들의 시체, 주변에 도끼로 찍어내린 듯한 자국, 역시 그 소녀가 벌인 짓이야."
    "그럼 스칼라부터 찾는 게 좋겠지. 포탈은 어떻게 열었는지, 리스는 왜 노리는지 알아봐야겠어."
    mys "으으으..."
    "뭐야, 어디서 사람 숨소리가 나지막이 들리는데? "
    "저기 '에너지 실험실'이라 적혀 있는 방 쪽에 있는 것 같아. 생존자야!"
    play sound "audio/sfx/lab door open2.ogg" volume 0.8
    scene c4-3 with change007
    #[장소3  리저렉션 라이프 랩  에너지 실험실]
    my "괜찮으세요?!"
    show scg_officer shake sick middle with dissolve:
        matrixcolor TintMatrix("#131313") * SaturationMatrix(0.7)  
    of "...누구?"
    my "일단 상처부터 치료해야 해야 될 것 같아요. 응급 키트가 배치된 곳이 어디죠?"
    show scg_officer sick middle with fastdissolve
    of "저기..."
    "힘겹게 가리킨 연구원의 손가락은 실험 테이블 위쪽에 비치된 서랍이었다."
    "보니까 '응급 키트'라 적힌 라벨도 붙어 있네. 저걸 열어서 꺼내 보면 되겠다."
    play sound "audio/sfx/fridge open.ogg"
    pause 0.5
    "안을 보니 헝겊과 붕대, 소독약 등 응급처치에 필요한 물품들은 다 들어있는 것 같아."
    "좋아, 이 정도면 급한 불을 끄는 데는 충분하겠어."
    play sound "audio/sfx/bandage.ogg"
    stop music fadeout 2.0
    #화면 암전 후 다시 켜짐
    scene black with dissolve
    scene c4-3 with change007
    play music "audio/music/science 2.ogg" fadein 2.0
    my "자, 다 됐어요."
    show scg_officer normal with dissolve
    of "가, 감사합니다..."
    "일시적 치료에 불과하지만, 그래도 상처를 어느 정도 손 본 덕이었을까, 연구원 분의 안색이 살짝이나마 좋아진 것 같아."
    my "누구한테 해를 당하신 건지 물어볼 수 있을까요?"
    show scg_officer shake curious middle with fastdissolve
    of "보라 머리에... 제복 차림을 한 여자였어요. "
    of "몸은 온통 피투성이였고, 비명을 질러댔죠."
    "그래, 지금 당장 이런 짓을 벌인 사람이 스칼라 아니면 누구겠냐."
    show scg_officer sick with fastdissolve
    of "사실... 그 애가 여기로 온 것은 이번이 두 번째예요."
    my "두 번째요?"
    of "몇 시간 전에도 여길 왔었거든요. 그때도 같은 포탈로 왔고..."
    show scg_officer shake curious middle with fastdissolve
    of "여기는 극비로 운영되는 연구소라 특정인이 아니면 출입이 불가능한 곳인데... 어떻게 들어온 건지."
    # (최신 포탈 기술을 연구 중인 포탈 연구소였다. 스칼라는 이 포탈을 통하면 분명 한국으로 갈 수 있다 믿었기 때문)
    my "그래서 제대로 된 대응이 안 되었던 거군요."
    of "그때 중요한 실험을 하는 날이라 거의 모든 연구원이 여기 실험실에 몰려 있었죠."
    of "그래서 방 하나에 수많은 시체가 널린 거고요."
    my "살려고 도망을 시도한 동료도 보셨겠군요..."
    show scg_officer shake sick middle with fastdissolve
    of "저도 도망칠 수 있었지만, 불청객을 보면 절대 가만히 있을 수 없는 성격이라서요. "
    of "어떻게든 막아보려고 제압을 시도했는데... 이런 꼴이 되어버렸죠."
    my "그렇군요..."
    show scg_officer shake curious middle with fastdissolve
    of "근데 여긴 어떻게 오신 거죠?"
    my "과부하 중인 포탈을 멈추기 위해 왔어요. "
    my "전원을 꺼서 일단 멈추긴 했는데, 어떻게 돌아갈지 모르겠더라고요."
    show scg_officer normal with fastdissolve
    of "아, 그건 간단해요. 재가동시켜 좌표를 찾아서 돌아가면..."
    my "상식적으로는 아는데, 제가 제어 장치에 대해서는 문외한이라 가지고요."
    show scg_officer shake curious middle with fastdissolve
    of "걱정 안 하셔도 됩니다. 이런 분야에는 제 전문이거든요!"
    show scg_officer normal with fastdissolve
    of "포탈이 있는 방으로 갑시다. 해결해 드릴게요."
    play sound "audio/sfx/lab door open.ogg"

    #[장소4 – 리저렉션 라이프 랩 - 제5포탈룸]

    scene c4-4 with change020
    show scg_officer normal with dissolve
    of "조금만 기다려주세요. 제어 장치를 재부팅시키는 데 오래 걸리지는 않으니까요."
    play sound "audio/sfx/typing.ogg"
    hide scg_officer normal with dissolve
    play sound "audio/sfx/typing.ogg" volume 0.7
    "역시 이런 쪽에 종사하시는 분이셔서 그런지, 키보드 두들기시는 소리가 남다르네."
    "기계에 문제가 있으면 해결할 수 있는 알고리즘을 머리 속에 다 기억하고 있는 거겠지."
    "...맞다. 그러고 보니 아직 스칼라가 이곳에 있는 것도 문제잖아. 연구원을 살리고 돌아가는 데 정신이 팔려 까먹을 뻔했어."
    "나도 그 문제를 해결할 방법을 생각해야 하나."
    play sound "audio/sfx/select button2.ogg"
    jump chapter1_4_select

label chapter1_4_select:
    scene c4-4 with change020
    show scg_officer normal with dissolve
    #선택지
    menu:
        "선택지1 : 스칼라를 찾는다 - 보안 카메라 탐색":  
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_normal

        "선택지2 : 스칼라를 찾는다 - 연구원의 증언":
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_true
            
        "선택지3 : 포탈이 재가동될 때까지 기다린다.":
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_bad

label chapter1_4_select_re:
    scene c4-4 with flash
    play music "audio/music/science 2.ogg" fadein 2.0
    #선택지
    menu:
        "선택지1 : 스칼라를 찾는다 - 보안 카메라 탐색":  
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_normal

        "선택지2 : 스칼라를 찾는다 - 연구원의 증언":
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_true
            
        "선택지3 : 포탈이 재가동될 때까지 기다린다.":
            play sound "audio/sfx/click button2.ogg"
            jump chapter1_4_bad
        
#[선택지1(노멀 엔딩) : 스칼라를 찾는다 - 보안 카메라 탐색] 선택 시 
label chapter1_4_normal: 

    #[장소1 – 리저렉션 라이프 랩 – 제5포탈룸]

    my "혹시 보안 카메라가 있는 곳이 어디죠?"
    show scg_officer normal with fastdissolve
    of "보안실 말씀하시는 거면 여기서 오른쪽 끝까지 가시면 되요."
    my "아, 감사합니다. 전 그 애부터 찾아서 처리한 후에 다시 돌아오도록 할게요."
    show scg_officer shake curious middle with fastdissolve
    of "잠깐만, 잡으러 가신다고요?"
    my "걱정 마세요. 제게 이런 건 일도 아닙니다."
    of "그래도 조심하셔야 할 거예요. 일반 병사하고는 차원이 달라 보이던데."
    my "저도 그런 애들을 수도 없이 만나봤죠. 금방 끝내고 올게요."
    show scg_officer normal with fastdissolve
    of "...네!"
    #[검은 화면]
    scene black with dissolve
    play sound "audio/sfx/lab walk.ogg" fadein 1.0 volume 1.4
    "계단을 타고 3층으로 올라가면 있다고 했나. 304호라 적혀있는 곳이..."
    "아, 저기 적혀 있네. '304호 보안실'이라고."
    stop music fadeout 2.0
    play sound "audio/sfx/lab door open2.ogg" volume 0.8

    #[장소5 - 리저렉션 라이프 랩 - 보안실]
    scene c4-6 with change020
    play music "audio/music/science 1.ogg" fadein 2.0
    "이야, 여기에 모니터란 모니터는 죄다 깔렸네. 역시 요런 데는 카메라가 많으니까."
    "마침 영상 위에 어떤 방인지도 알려주네. "
    "'제1포탈룸', '제2포탈룸' 이렇게... 보니까 포탈이 있는 방이 제법 많네."
    "좋아, 채널을 통해 스칼라의 위치를 한 번 찾아볼까."

    jump chapter1_4_1_a

label chapter1_4_1_a:

    scene c4-6 with dissolve

    $ channel = renpy.input("찾고자 하는 채널을 적어주세요.(1번~3번, 없으면 엔터키를 누르세요.)", length =40)  


    if channel == "1번":
        play sound "audio/sfx/cctv.ogg"
        show tv1 with change007
        ch_na "여긴 또다른 연구실인가... 아까 다닌 곳하고 비슷해보이네."
        "이곳에 스칼라는 없는 거 같아."
        call chapter1_4_1_a
    #이름이 없을 때
    elif channel == "2번":
        play sound "audio/sfx/cctv.ogg"
        show tv2 with change007
        ch_na "여긴 자료실인가봐. 서적이 수도없이 배치되어  있어."
        "이런 곳에 스칼라가 있을 리는 없겠지? 뭐하러 저런 걸 읽으려 가겠어."
        call chapter1_4_1_a

    elif channel == "3번":
        play sound "audio/sfx/cctv.ogg"
        show tv3 with change007
        ch_na "아까 봤던 곳이구나. 다시 돌아오지는 않았네."
        "대체 어디에 꽁꽁 숨어있는 걸까."
        call chapter1_4_1_a

    elif channel == "":
        jump chapter1_4_1_b

    else:
        play sound "audio/sfx/type error.ogg"
        ch_na "{color=#0aa6ff}<error01 - 잘못 입력하셨습니다. 정확하게 입력해주세요.>{/color}"
        call chapter1_4_1_a

label chapter1_4_1_b:
    scene c4-6 with change020
    "으음... 역시 머리가 아프네. 수십 곳을 혼자서 한꺼번에 확인한다는 게 참 쉽지가 않지."
    "스칼라 대신 보이는 사람들은 방 곳곳에 널려 있는 연구원들의 시체일 뿐."
    "살아있는 사람은 아까 치료해줬던 연구원 분 말곤 없는 것 같다. "
    "근데 가만... 화면이 꺼진 곳도 있네? 그 채널은 신호가 끊긴 건가?"
    "그러고 보니 한 가지 이상한 부분이 있어."
    play sound "audio/sfx/mouse click.ogg"
    pause 1.0
    "없다. 연구원 분이 나오는 채널이 없어."
    "그 분이 지금 계신 곳도 카메라 신호가 끊겼다는 건가?"
    stop music fadeout 1.0
    play sound "audio/sfx/error.ogg" fadein 1.0 volume 0.5
    with Shake((0, 0, 0, 0), 0.8, dist=30)
    pause 1.2
    play music "audio/music/lab warning.ogg" volume 2.5
    scene c4-6 with dissolve:
        matrixcolor TintMatrix("#b6008e") * SaturationMatrix(0.8)
    "젠장! 또 무슨 일이 터진 것 같아! 설마 작동 과정 중에 잘못된 게 있나?"
    #[검은 화면]
    scene black with dissolve
    "{color=#0aa6ff}<경고. 허가되지 않은 포탈이 가동되었습니다.>{/color}"
    
    #[장소6 – 리저렉션 라이프 랩 – 제5포탈룸]
    play sound "audio/sfx/lab door open2.ogg" volume 0.8
    scene c4-4 with change020:
        matrixcolor TintMatrix("#b6008e") * SaturationMatrix(0.8)
    show scg_scala shake happy middle with dissolve:
        matrixcolor TintMatrix("#1f0018") * SaturationMatrix(0.5) 

    s "...오오."
    "다시 돌아와 보니, 나를 맞이하는건 치료했던 연구원 대신 스칼라였다."
    "웃음기가 다시 돌아온 걸 보면 뭔가 저지른 것 같아. 설마...!"
    my "그 여자를 어떻게 한 거지?"
    show scg_scala happy with dissolve:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    s "저쪽으로..."
    "스칼라가 손가락으로 가리킨 건 다시 가동된 포탈이었다. 저기다 내던졌다 이거야?"
    "내가 잠시 자리를 뜨던 사이에 이런 일을 벌였다라..."
    pause 0.5
    "...일단 진정하자. 흥분하면 페이스를 잃고 당할 수 있어."
    show scg_scala smile with fastdissolve
    s "너도... 저쪽으로 보내주지."
    my "누구 맘대로."
    show scg_scala shake happy middle with fastdissolve
    s "{size=+18}내 맘대로!"
    play sound "audio/sfx/hit.ogg" fadein 0.3
    with Shake((0, 0, 0, 0), 0.4, dist=30)
    "역시, 노웰하고 싸웠을 때랑 비슷해. 스피드가 장난이 아니야."
    "여기서 공격을 피하고 빈틈을 찾아 베는 걸로 해야겠어."
    play sound "audio/sfx/scala attack.ogg" fadein 1.0
    with vpunch
    "몸을 숙여 도끼를 피했을 때, 왼쪽 옆구리에 빈틈이 보였다."
    "이때가 찬스야! 바로 역습을 가하면!"
    stop music fadeout 1.0
    "-툭."
    show scg_scala shake silly middle with fastdissolve
    s "응...?"
    "뭐야, 분명 검에 힘을 꽉 쥐고 휘둘렀는데."
    "왜 세 살 아이가 휘날리는 장난감 검 같이... 베지도 못하고 그냥 툭 건드린 수준이잖아?"
    "어떻게 된 거지? 새로운 육체의 영향인가?"
    show scg_scala smile with fastdissolve
    s "하... 겨우?"
    play music "audio/music/lab warning2.ogg" fadein 1.0
    play sound "audio/sfx/mental crash.ogg" fadein 1.0 volume 0.7
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "젠장, 얼마나 큰 충격이었는지 등이 너무 아파! 몸을 일으키지도 못하겠어!"
    "팔저림도 몰려와 검도 떨어뜨렸어. 젠장, 이건 내 예상과 완전히 빗나간 상황인데."
    show scg_scala happy with fastdissolve
    s "금방 보내줄게~?"
    play sound "audio/sfx/scala attack.ogg" fadein 1.0
    with vpunch
    "피할 겨를도, 당장 검을 쥘 겨를도 없다. 어떻게든 저 도끼를 막아야 해!"
    "뻗어, 빨리 팔을 뻗으라고! 안 그러면 내 머리가 두 동강이 날 거야!"
    "{size=+13}그때처럼 당할 거야? 무능하게 있을 거냐고!"
    stop music fadeout 1.0



    play sound "audio/sfx/flash.ogg"
    #화면이 잠시 하얘지는 효과
    show c4-4 with flash
    show scg_scala shake silly middle with fastdissolve
    s "윽...!!"
    "그 순간, 내 심장 안에서 이상한 기운이 요동치기 시작했다."
    "어제 푸른 공간 안에서 느꼈던 기운과 비슷해. 뭔가 내보내고 싶은 느낌이 드는데?"

    play music "audio/music/scala battle 2.ogg" fadein 2.0
    play sound "audio/sfx/grab.ogg" 
    with vpunch
    s "...뭐야! 내 무기를!"
    "잡은 도끼에 힘을 쥐었더니 금도 가기 시작했다. "
    "방금 요동쳤던 기운의 영향인가. 내 힘의 원천이 되어주고 있는 것 같아."
    show scg_scala very angry with fastdissolve
    s "이거 놔! 놓으라고!"
    "스칼라도 내 변수에 당황한 것일까. 좋아, 그럼 어디 한 번...!"
    play sound "audio/sfx/punch.ogg" volume 1.4
    show scg_scala very angry middleout with fastdissolve
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    play sound "audio/sfx/wall break.ogg"
    s "크아아악!!"
    "망설임 없이 주먹을 내지르자, 벽 쪽으로 바로 내몰았다."
    "이번엔 공격이 제대로 먹혔으니 온갖 고통으로 가득 베여 있겠지. 연구원에게 위해를 끼친 대가다, 이놈아."
    show scg_scala sick topin with fastdissolve
    s "으으으... "
    stop music fadeout 10.0
    show scg_scala sick topout with fastdissolve
    play sound "audio/sfx/body fall.ogg"
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "그래, 상처 덕분에 팔다리가 힘이 빠질 거라 알고 있었어. 결국 정신을 잃었구만."
    "원래라면 이 상황에서 제거하는 게 정상이긴 해. 방금 연구원 분의 생사를 알 수 없게 만들었으니까."
    "허나 일단 리스의 친구라고 하니, 이 정도쯤 하는 게 최선이겠지."
    play sound "audio/sfx/toxic gas.ogg"
    pause 1.0
    show c4-4 with dissolve:
        matrixcolor TintMatrix("#00dd81") * SaturationMatrix(0.5)
    play music "audio/music/gas warning.ogg" 
    "{color=#0aa6ff}<경고. 치명적인 유해물질이 감지되었습니다.>{/color}"
    "에이 씨, 갑자기 어디서 유독가스가 들어온 거야! "
    "입으로 틀어막아도 틈새로 다 들어오네. 다 된 밥에 재를 뿌리는 격이잖아?"
    "제, 젠장, 문을 열어 빠져나와야 하는데 너무 어지러워..."
    stop music fadeout 3.0
    scene black with eyecloseslow
    #[검은 화면]
    pause 1.0
    play sound "audio/sfx/typing3.ogg"
    "{color=#0aa6ff}<시스템 및 좌표 복구 완료. 생존자의 자동 이송을 실행합니다.>{/color}"
    play sound "audio/sfx/portal out.ogg"


    #[장소9 - 시내] 
    scene c3-4 with flash
    pause 1.0
    play music "audio/music/castle1.ogg" fadein 1.0
    show scg_nowell2 curious leftin with fastdissolve
    n "...왔다!"
    n "괜찮아? 정신이 들어?"
    "뭐, 뭐야... 다시 이쪽으로 돌아온 거야?"
    "바로 저 앞에 노웰과 리스의 모습도 보이고. 이게 어떻게 된 거지?"
    "일단 연구원 분한테는 미안하다고 전할게요. 제가 생각을 좀 더 신중히 했어야 했는데..."
    show scg_reese3 walk rightin with fastdissolve
    r "참 멀리도 갔다왔구마. 에르온은 어떻냐?"
    my "제, 제대로 구경도 못 하고 떠났어. 문제 해결에 급급해서."
    show scg_reese3 wink smile right with fastdissolve
    r "후훗, 이때다 싶어 도망칠 생각은 읎었구마. 설령 그런다 혀도 아무 소용 읎지만."
    r "잘혔다. 요 시내를 구한 영웅 납셨네."
    "현장을 다시 보니 주위에 있던 민간인들은 다 떠나고, 사건 처리를 위한 공무집행 요원들만 보이네."
    "방금 일어났던 일이 없었던 것 같아."
    show scg_reese3 close eyes right with fastdissolve
    r "아, 그리고 노웰한테 얘기 들었다. 둘이서 스칼라를 만났다고."
    my "그랬지. 주인 친구라며."
    show scg_reese3 normal right with fastdissolve
    r "은제부터 상태가 삐뚤어졌는지 모르겠구마. 저럴 애가 아닌디..."
    my "그 애를 원래대로 되돌려놓을 수 있을까?"
    show scg_nowell2 close eyes sad left with fastdissolve
    n "그러기에는 지금 정보가 별로 없어. "
    n "계속 추적해보거나, 아님 다시 돌아왔을 때 제대로 잡는 수밖에."
    my "그때 내가 발목을 꽉 묶어놨어야 했나."
    show scg_nowell2 smile left with fastdissolve
    n "하핫...! 놓쳤나 보구나. 얼마 안 가 다시 오겠지."
    my "참 지치지도 않나, 걔는."
    show scg_reese3 angry right with fastdissolve
    r "나가 여그 있는 한 절대 지칠 애가 아니다. 내 목숨이 곧 걔가 살아가는 이유나 마찬가지니."
    my "...그러겠지."
    show scg_nowell2 normal left with fastdissolve
    n "자, 자! 일단 돌아가자!"
    n "우리 영웅님께서 무사귀환하셨으니 비싼 레스토랑을 예약해야겠군!"
    "세상 살기 참 어려워. 특히나 새로운 곳에서 살림을 꾸린다는 건 막막하지."
    "아직도 그 막막함이 완전히 사라진 건 아니지만, 한 가지 깨달은 게 있다."
    "뭐든지 도전하고자 하는 마음을 가진다면 분명 길이 트일 거라는 것, 그런 생각이 지금 막 생겼다고 해야 할까."
    "새로운 도전은... 앞으로 나아갈 열쇠이기도 하잖아."
    stop music fadeout 2.0
    jump chapter1_5_normal


#[선택지2(트루 엔딩) : 스칼라를 찾는다 - of의 증언] 선택 시
label chapter1_4_true: 

    "일단 습격당한 과정에 대해 좀 더 물어봐야겠다. 알고 계신 게 더 있으실지도 몰라."
    my "혹시 그 여자와 싸움이 났을 때 뭐라 말한 게 있나요?"
    show scg_officer curious with fastdissolve
    of "전부 처리한 후에 특정 단어를 반복하며 자리를 떴어요. '약, 약...' 이러면서요."
    my "그럼 약품이 있는 데로 간 건가요?"
    show scg_officer normal with fastdissolve
    of "계단 아래로 내려가면 약품보관실이 있긴 해요. 그쪽으로 갔을지도 모르겠네요."
    my "네, 감사합니다."
    my "전 그 애부터 처리하고 다시 돌아오도록 할게요."
    show scg_officer curious with fastdissolve
    of "잠깐만, 잡으러 가신다고요?"
    my "걱정 마세요. 제게 이런 건 일도 아닙니다."
    of "그래도 조심하셔야 할 거예요. 일반 병사하고는 차원이 달라 보이던데."
    my "저도 그런 애들을 수도 없이 만나봤는데요, 뭐."
    my "금방 끝내고 오겠습니다."
    show scg_officer normal with fastdissolve
    of "...네!"

    #[검은 화면]
    scene black with dissolve
    stop music fadeout 2.0
    play sound "audio/sfx/lab walk.ogg" fadein 1.0 volume 1.4
    "계단을 타고 1층으로 올라가면 있다고 했나. 102호라 적혀있는 곳이..."
    #[장소5 - 리저렉션 라이프 랩 - 약품보관실]
    play sound "audio/sfx/lab door open2.ogg" volume 0.8
    stop music fadeout 1.0
    scene c4-7 with change007
    play music "audio/music/science 1.ogg" fadein 1.0
    show scg_scala shake happy middle with dissolve:
        matrixcolor TintMatrix("#1f0018") * SaturationMatrix(0.5) 
    s "...!!"
    "예상했던 바가 맞았어. 피투성이인 채로 계속 돌아다닐 수는 없겠지."
    "웬만한 캐비닛은 죄다 열은 흔적이 보였고."
    "바닥에는 알약에 물약에 주사기에... 아주 약과 관련된 건 죄다 널려 있네. 어떻게든 고통을 해소하기 위해 몸부림친 거겠지."
    show scg_scala happy with dissolve:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    s "피냄새, 리스 거..."
    my "그래, 아까 초록 머리랑 같이 붙어 있던 사람이야. 약기운 때문에 정신이 미쳐 돌아버리겠지?"
    show scg_scala very angry with fastdissolve
    s "...웃기지 마."
    "어딘가 몽롱해보이는 듯한 얼굴이 보이긴 하는데, 사나운 본능은 아직 잠들지 않았네."
    "아무리 정신상태가 안 좋아도 사냥감을 보게 되면 순식간에 목적을 깨닫고 확 물어뜯어 버릴 수도 있지."
    my "아무리 리스를 죽이고 싶어도 그렇지, 다른 사람까지 휘말리게 하면 어떡하니?"
    show scg_scala angry2 with fastdissolve
    s "짜증 나..."
    show scg_scala very angry with fastdissolve
    s "{size=+13}방해하는 놈들... 짜증 나!"
    play sound "audio/sfx/hit.ogg" fadein 0.3
    with Shake((0, 0, 0, 0), 0.4, dist=30)
    "역시, 노웰하고 싸웠을 때랑 비슷해. 스피드가 장난이 아니야."
    "여기서 공격을 피하고 빈틈을 찾아 베는 걸로 해야겠어."
    play sound "audio/sfx/scala attack.ogg" fadein 1.0
    with vpunch
    "몸을 숙여 도끼를 피했을 때, 왼쪽 옆구리에 빈틈이 보였다."
    "이때가 찬스야! 바로 역습을 가하면!"
    
    
    
    stop music fadeout 1.0
    play sound "audio/sfx/break.ogg"  volume 0.2
    pause 1.0
    show scg_scala shake silly middle with fastdissolve
    s "응...?"
    "뭐야, 분명 검에 힘을 꽉 쥐고 휘둘렀는데."
    "왜 세 살 아이가 휘날리는 장난감 검 같이... 베지도 못하고 그냥 툭 건드린 수준이잖아?"
    "어떻게 된 거지? 새로운 육체의 영향인가?"
    show scg_scala smile with fastdissolve
    s "하... 겨우?"
    play music "audio/music/lab warning2.ogg" fadein 1.0
    play sound "audio/sfx/mental crash.ogg" fadein 1.0 volume 0.7
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "젠장, 얼마나 큰 충격이었는지 등이 너무 아파! 몸을 일으키지도 못하겠어!"
    "팔저림도 몰려와 검도 떨어뜨렸어. 젠장, 이건 내 예상과 완전히 빗나간 상황인데."
    show scg_scala happy with fastdissolve
    s "금방 보내줄게~?"
    play sound "audio/sfx/scala attack.ogg" fadein 1.0
    with vpunch
    "피할 겨를도, 당장 검을 쥘 겨를도 없다. 어떻게든 저 도끼를 막아야 해!"
    "뻗어, 빨리 팔을 뻗으라고! 안 그러면 내 머리가 두 동강이 날 거야!"
    "{size=+13}그때처럼 당할 거야? 무능하게 있을 거냐고!"
    stop music fadeout 1.0



    play sound "audio/sfx/flash.ogg"
    #화면이 잠시 하얘지는 효과
    show c4-7 with flash
    show scg_scala shake silly middle with fastdissolve
    s "윽...!!"
    "그 순간, 내 심장 안에서 이상한 기운이 요동치기 시작했다."
    "어제 푸른 공간 안에서 느꼈던 기운과 비슷해. 뭔가 내보내고 싶은 느낌이 드는데?"

    play music "audio/music/scala battle 2.ogg" fadein 2.0
    play sound "audio/sfx/grab.ogg" 
    with vpunch
    s "...뭐야! 내 무기를!"
    "잡은 도끼에 힘을 쥐었더니 금도 가기 시작했다. "
    "방금 요동쳤던 기운의 영향인가. 내 힘의 원천이 되어주고 있는 것 같아."
    show scg_scala very angry with fastdissolve
    s "이거 놔! 놓으라고!"
    "스칼라도 내 변수에 당황한 것일까. 좋아, 그럼 어디 한 번...!"
    play sound "audio/sfx/punch.ogg" volume 3.0
    show scg_scala very angry middleout with fastdissolve
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    play sound "audio/sfx/wall break.ogg" volume 2.5
    s "크아아악!!"
    "망설임 없이 주먹을 내지르자, 벽 쪽으로 바로 내몰았다."
    "이번엔 공격이 제대로 먹혔으니 온갖 고통으로 가득 베여 있겠지. 연구원에게 위해를 끼친 대가다, 이놈아."
    show scg_scala sick topin with fastdissolve
    s "으으으... "
    stop music fadeout 10.0
    show scg_scala sick topout with fastdissolve
    play sound "audio/sfx/body fall.ogg"
    with Shake((0, 0, 0, 0), 0.6, dist=30)
    "그래, 상처 덕분에 팔다리가 힘이 빠질 거라 알고 있었어. 결국 정신을 잃었구만."
    "원래라면 이 상황에서 제거하는 게 정상이긴 해. 방금 연구원 분의 생사를 알 수 없게 만들었으니까."
    "허나 일단 리스의 친구라고 하니, 이 정도쯤 하는 게 최선이겠지."
    play sound "audio/sfx/toxic gas.ogg"
    pause 1.0
    show c4-7 with dissolve:
        matrixcolor TintMatrix("#00dd81") * SaturationMatrix(0.5)
    play music "audio/music/gas warning.ogg" 
    "{color=#0aa6ff}<경고. 치명적인 유해물질이 감지되었습니다.>{/color}"
    "에이 씨, 갑자기 어디서 유독가스가 들어온 거야! "
    "입으로 틀어막아도 틈새로 다 들어오네. 다 된 밥에 재를 뿌리는 격이잖아?"
    "제, 젠장, 문을 열어 빠져나와야 하는데 너무 어지러워..."
    stop music fadeout 3.0
    scene black with eyecloseslow

    #[검은 화면]
    #[장소6 - 리저렉션 라이프 랩 - 옥상 테라스]
    mys "...괜찮으세요?"
    my "여, 여긴..."
    play music "audio/music/terrace 1.ogg" fadein 2.0
    scene officer memorial with flash:
        matrixcolor TintMatrix("#ffc3f1") * SaturationMatrix(0.8) 
    image moon bubble = Fixed(SnowBlossom("gui/moon bubble.png", 120, xspeed=(20, 60), yspeed=(50, 400), start=20))
    show moon bubble
    of "조금 전에 유독가스가 흘러나와 옥상 테라스까지 옮겨다 드렸어요."
    "테라스라... 여기로 오니 창문 너머에서도 본 경치가 확 와닿네."
    of "부팅 끝나고 보안 카메라실로 가서 상황을 분석했는데, 그 소녀가 가스탄을 발전소실에 넣은 모습이 있더라고요."
    my "일정시간이 지나면 터지게끔 하는 가스탄이었던 거였군요. 그 소녀는 제가 쓰러진 곳에 같이 있었나요?"
    of "아뇨, 제가 왔을 때는 없었어요."
    "없었다면 설마 도망쳤나? 정신을 잃은 와중에 그 가스를 들이마시며 도망치는 게 가능한 일인가."
    "아님 이 상황을 노리고 일부러 기절한 척을 했을 수도... 잔머리 하나는 잘 굴리네."
    scene c4-5 with change007
    show scg_officer normal with dissolve
    of "어디로 돌아가신다 하셨죠?"
    my "한국이요. 에르온과는 다른 행성에 속한 땅 중에 하나입니다."
    show scg_officer shake curious middle with fastdissolve
    of "한국... 이라고요? 그건 처음 들어보는데. 어느 행성에 있는 거죠?"
    my "지구라는 곳에 있습니다."
    show scg_officer normal with fastdissolve
    of "아아, 지구! 태양계 중에 세 번째로 떠돌아다닌다는 그 행성 맞나요?"
    my "그럴 겁니다."
    of "원래 그쪽에서 사시는 분이신가 봐요."
    my "아니요, 원래 에르온에서 살았는데, 어쩌다가 지구로 넘어갔습니다."
    show scg_officer shake curious middle with fastdissolve
    of "그렇다면 돌아가실 건가요?"
    my "네, 할 일도 있고 하니 그럴 예정입니다."
    show scg_officer normal2 with fastdissolve
    of "웬지 그러실 것 같더라고요. 마침 좌표가 복구된 참이었는데."
    my "오, 그런가요?"
    show scg_officer shake curious middle with fastdissolve
    of "원하실 때 타시고 돌아가시면 됩니다. 장치는 열려 있어요."
    my "감사합니다. 덕분에 집으로 돌아가겠네요."
   
   
    scene c4-4 with change007
    show scg_officer shake curious middle with fastdissolve
    my "그쪽도 돌아가시려는 거죠?"
    show scg_officer normal2 with fastdissolve
    of "네. 병원도 가봐야 하고, 상황 보고도 해야죠."
    show scg_officer normal with fastdissolve
    of "조심히 가세요. 하시는 일 잘 되시길 기원할게요."
    my "감사합니다. 그럼..."
    play sound "audio/sfx/portal in.ogg"
    stop music fadeout 2.0
   
    #[장소7 - 시내] 
    scene c3-4 with flash
    pause 1.0
    show scg_nowell2 curious leftin with fastdissolve
    play music "audio/music/castle3.ogg" fadein 1.0
    n "...왔다!"
    n "여기야! 이쪽!"
    "후우... 제대로 돌아갈 수 있나 걱정되긴 했는데, 다행이 무사히 돌아왔네."
    show scg_reese3 walk rightin with fastdissolve
    r "참 멀리도 갔다왔구마. 에르온은 어떻냐?"
    my "제, 제대로 구경도 못 하고 떠났어. 문제 해결에 급급해서."
    show scg_reese3 wink smile right with fastdissolve
    r "후훗, 이때다 싶어 도망칠 생각은 없었구마. 설령 그런다 혀도 아무 소용 없지만."
    r "잘혔다. 요 시내를 구한 영웅 납셨네."
    "현장을 다시 보니 주위에 있던 민간인들은 다 떠나고, 사건 처리를 위한 공무집행 요원들만 보이네."
    "방금 일어났던 일이 없었던 것 같아."
    show scg_reese3 close eyes right with fastdissolve
    r "아, 그리고 노웰한테 얘기 들었다. 둘이서 스칼라를 만났다고."
    my "그랬지. 주인 친구라며."
    show scg_reese3 normal right with fastdissolve
    r "은제부터 상태가 삐뚤어졌는지 모르겠구마. 저럴 애가 아닌디..."
    my "그 애를 원래대로 되돌려놓을 수 있을까?"
    show scg_nowell2 close eyes sad left with fastdissolve
    n "그러기에는 지금 정보가 별로 없어. "
    n "계속 추적해보거나, 아님 다시 돌아왔을 때 제대로 잡는 수밖에."
    my "그때 내가 발목을 꽉 묶어놨어야 했나."
    show scg_nowell2 smile left with fastdissolve
    n "하핫...! 놓쳤나 보구나. 얼마 안 가 다시 오겠지."
    my "참 지치지도 않나, 걔는."
    show scg_reese3 angry right with fastdissolve
    r "나가 여그 있는 한 절대 지칠 애가 아니다. 내 목숨이 곧 걔가 살아가는 이유나 마찬가지니."
    my "...그러겠지."
    show scg_nowell2 normal left with fastdissolve
    n "자, 자! 일단 돌아가자!"
    n "우리 영웅님께서 무사귀환하셨으니 비싼 레스토랑을 예약해야겠군!"
    "세상 살기 참 어려워. 특히나 새로운 곳에서 살림을 꾸린다는 건 막막하지."
    "아직도 그 막막함이 완전히 사라진 건 아니지만, 한 가지 깨달은 게 있다."
    "뭐든지 도전하고자 하는 마음을 가진다면 분명 길이 트일 거라는 것, 그런 생각이 지금 막 생겼다고 해야 할까."
    "새로운 도전은... 앞으로 나아갈 열쇠이기도 하잖아."
    stop music fadeout 2.0
    jump chapter1_5_true
    
#[선택지3(배드 엔딩) : 포탈이 재가동될 때까지 기다린다.] 선택 시
label chapter1_4_bad: 

    "아니야, 포탈이 재가동될 때까지 한 번 기다려보자."
    "그리 오래 걸리진 않는다 하셨으니까... 일단 다시 가동되면 연구원 분부터 보내고 내 갈 길 가면 될 것 같아."
    "설령 걔가 이쪽에 온다 해도 발소리는 들릴 테니 나가서 근처에 못 가게 막으면 되고."
    play sound "audio/sfx/boot up.ogg"
    pause 1.0
    show scg_officer normal topin 
    of "아, 부팅에 성공했네요."
    show scg_officer shake curious middle with fastdissolve
    of "어디 보자, 포탈 사용 내역이..."
    play sound "audio/sfx/toxic gas.ogg"
    pause 1.0
    show c4-4 with dissolve:
        matrixcolor TintMatrix("#00dd81") * SaturationMatrix(0.5)
    play music "audio/music/gas warning.ogg" 
    show scg_officer shake sick middle with dissolve:
        matrixcolor TintMatrix("#00dd81") * SaturationMatrix(0.5)
    of "...뭐야?!"
    "{color=#0aa6ff}<경고. 치명적인 유해물질이 감지되었습니다.>{/color}"
    of "망할, 어디서 유독가스가 들어온 거야!"
    of "문을, 문부터 열어야..."
    show scg_officer sick topout
    play sound "audio/sfx/body fall.ogg"
    with vpunch
    
    "젠장, 너무 어지러워... 머리가 깨질 것 같아..."
    hide scg_officer sick topout
    "돌아온다고 약속을 했는데..."
    stop music fadeout 2.0
    scene black with eyecloseslow
    #[검은 화면]
    s "크흐흐흐..."
    jump chapter1_5_bad

label chapter1_5_bad:
    scene bad ending with dissolve
    show messian bad topin:
        matrixcolor TintMatrix("#00814b") * SaturationMatrix(0.5)
    "{color=#0bb9d8}[povname]{/color}은 슬픈 결말을 맞았습니다..."
    jump chapter1_5_bad_select


label chapter1_5_bad_select:
    $ back = renpy.input("선택지로 돌아가시겠습니까?(예, 아니오)", length =40)
        
    if back == "예":
        ch_na "{color=#0aa6ff}<이전 선택지 화면으로 돌아갑니다.>{/color}"
        play sound "audio/sfx/portal in.ogg"
        call chapter1_4_select_re

    elif back == "아니오":
        ch_na "{color=#0aa6ff}<초기 화면으로 돌아갑니다.>{/color}"
        jump ch_select

    else:
        ch_na "{color=#0aa6ff}<error01 - 잘못 입력하셨습니다. 정확하게 입력해주세요.>{/color}"
        call chapter1_5_bad_select

    scene black with eyecloseslow
    jump chapterend


label chapter1_5_normal:
    scene normal ending with flash
    pause 0.5
    play music "audio/music/ending2.ogg" fadein 1.0
    play sound "audio/sfx/clear.ogg"
    "{color=#0bb9d8}[povname]{/color}은 괜찮은 결말을 맞았습니다."
    scene black with flash
    jump chapterend


label chapter1_5_true:
    scene true ending with flash
    pause 0.5
    play music "audio/music/ending2.ogg" fadein 2.0
    play sound "audio/sfx/clear.ogg" volume 0.2
    "{color=#0bb9d8}[povname]{/color}은 진정한 결말을 맞았습니다!"
    jump chapterend


label chapterend:
    $ channel = renpy.input("엔터키를 누르시면 목차선택으로 돌아갑니다.(엔터키를 누르세요.)", length =40)  

    if channel == "":
        stop music fadeout 1.0
        jump ch_select

    else:
        ch_na "{color=#0aa6ff}<error01 - 잘못 입력하셨습니다. 정확하게 입력해주세요.>{/color}"
        jump ch_select
    return