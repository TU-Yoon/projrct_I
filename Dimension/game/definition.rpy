#이 코드는 캐릭터, 배경, 효과 등을 정의하는 코드입니다.


# 이미지를 정의합니다.
#image hiyori_m01 = "hiyori_m01.png"
image black = "bg/black.png"

image p1 = "bg/p1.png"
image p2 = "bg/p2.png"
image p3 = "bg/p3.png"
image p4 = "bg/p4.png"
image p5 = "bg/p5.png"
image p6 = "bg/p6.png"

image c1-1 = "bg/c1-1.png"
image c1-2 = "bg/c1-2.png"
image c1-3 = "bg/c1-3.png"

image c2-1 = "bg/c2-1.png"
image c2-2 = "bg/c2-2.png"
image c2-3 = "bg/c2-3.png"
image c2-4 = "bg/c2-4.png"

image c3-2 = "bg/c3-2.png"
image c3-3 = "bg/c3-3.png"

image reese memorial = "bg/reese memorial.png"

define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 1.5)
define right2 = Position(xalign = 0.9)
define left2 = Position(xalign = 0.1)

image vacuum cleaner:
    im.FactorScale("ch/vacuum cleaner.png", 1.0)
    yalign 0.0



image scg_reese1:
    im.FactorScale("ch/reese/scg reese test.png", 1.0)
    yalign 0.0


image scg_reese1 shout:
    im.FactorScale("ch/reese/scg reese1 shout.png", 1.0)
    yalign 0.0


# 리스 평상 시 걸을 때 -> scg_reese normal walk
image scg_reese1 walk:
    im.FactorScale("ch/reese/scg reese test.png", 1.0)
    parallel:
        yalign 0.0
        easeout 1.5 yalign -0.05
        easeout 1.0 yalign 0.0
        repeat


# 리스가 화날 때 -> scg_reese angry
image scg_reese1 little smile:
    im.FactorScale("ch/reese/scg reese1 little smile.png", 1.0)
    yalign 0.0

image scg_reese1 silly:
    im.FactorScale("ch/reese/scg reese1 silly.png", 1.0)
    yalign 0.0

image scg_reese1 silly2:
    im.FactorScale("ch/reese/scg reese1 silly2.png", 1.0)
    yalign 0.0

image scg_reese1 happy:
    im.FactorScale("ch/reese/scg reese1 happy.png", 1.0)
    yalign 0.0

image scg_reese1 sad:
    im.FactorScale("ch/reese/scg reese1 sad.png", 1.0)
    yalign 0.0

image scg_reese1 close smile:
    im.FactorScale("ch/reese/scg reese1 close smile.png", 1.0)
    yalign 0.0

image scg_reese1 close eyes:
    im.FactorScale("ch/reese/scg reese1 close eyes.png", 1.0)
    yalign 0.0

image scg_reese1 refuse:
    im.FactorScale("ch/reese/scg reese1 close eyes.png", 1.0)
    parallel:
        xalign 0.55
        easein 0.5 xalign 0.45
        easeout 0.5 xalign 0.55
        repeat

image scg_reese1 shake smile:
    im.FactorScale("ch/reese/scg reese1 close smile.png", 1.0)
    parallel:
        xalign 0.5
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_reese1 silly smile:
    im.FactorScale("ch/reese/scg reese1 silly.png", 1.0)
    parallel:
        xalign 0.5
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_reese1 silly smile2:
    im.FactorScale("ch/reese/scg reese1 silly2.png", 1.0)
    parallel:
        xalign 0.5
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_reese1 shake close eyes:
    im.FactorScale("ch/reese/scg reese1 close eyes.png", 1.0)
    parallel:
        xalign 0.5
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_reese1 shake happy:
    im.FactorScale("ch/reese/scg reese1 happy.png", 1.0)
    parallel:
        xalign 0.5
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_reese1 shake happy right2:
    im.FactorScale("ch/reese/scg reese1 happy.png", 1.0)
    parallel:
        xalign 0.9
        easein 0.1 xalign 0.89
        easeout 0.1 xalign 0.91
        repeat 2

#노웰 스프라이트

image scg_nowell sports walk:
    im.FactorScale("ch/nowell/scg nowell sports normal.png", 1.5)
    #easein 0.8 yalign 0.0
    parallel:
        xalign 0.8
        yalign 0.0
        easein 1.5 yalign -0.05
        easeout 1.5 yalign 0.0
        repeat 2


image scg_nowell sports wink:
    im.FactorScale("ch/nowell/scg nowell sports wink.png", 1.5)
    parallel:
        xalign 0.8
        yalign 0.0
        easein 0.1 xalign 0.79
        easeout 0.1 xalign 0.81
        repeat 2


image bathroom night = "bg/bathroom.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('매시안', color="#0bb9d8")
define r = Character('리스', color="#ff0000")
define n = Character('노웰', color="#00ff04")
define mys = Character('???', color="#FFFFFF")
define my =  Character("[povname]", color="#0bb9d8")

# 독백은 ch_na로 고정(na는 형식상 존재)
define na = Character(None, kind = nvl)
define ch_na = Character(None)


#기타 인물 - 프롤로그
define fish = Character('생선 아줌마', color="#FFFFFF")
define bus = Character('버스 기사', color="#FFFFFF")
define del = Character('배달원', color="#FFFFFF")



## 효과 코드

define rightCharacter = Position(xpos = 800, yalign = 0.0)
define longer_easein = MoveTransition(0.3, enter=_movebottom, enter_time_warp=_warper.easein)

define lefttoright = MoveTransition(3.0, enter=_moveleft, enter_time_warp=_warper.easein)
define righttoleft = MoveTransition(1.0, enter=_moveright, enter_time_warp=_warper.easein)

#Fade(지속시간, 시작할 때의 투명도, 끝날 때의 투명도, color=색상)

define slowfade = Fade(3, 1, 0.75, color="#fff")
#flash = 반짝이는 연출
define flash = Fade(2, 0, .75, color="#fff")
define fastflash = Fade(0.01, 0, 1, color="#fff")
define redflash = Fade(0.01, 0, 0.5, color="#b30e3f")

#eclipsy = 깜빡이는 연출
define eclipsy = Fade(0.01, 0, 1, color="#ddf4ff")
define eclipsy2 = Fade(1, 0, 1, color="#ddf4ff")
define eclipsy3 = Fade(0.5, 0, 1, color="#ffffff")
define eclipsy4 = Fade(0.3, 0, 1, color="#ffffff")

# eyeclose = 눈이 감기는 연출
define eyeclose = Fade(3, 0, 1, color="#000000")

# eyecloseslow = 눈이 천천히 감기는 연출(추가)
define eyecloseslow = Fade(3, 1.5, 1, color="#000000")

define collect = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.125)

define fastdissolve = Dissolve(0.1) 

define change020 = ImageDissolve("change scene/020.jpg", 2.0, ramplen=256)
define change007 = ImageDissolve("change scene/007.png", 2.0, ramplen=256)


#청소 포인트
init:
    $ Test_point = 0

#Shake(화면 흔들기)
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #

define mymatrix = Matrix([ 1.0, 0.0, 0.0, 0.0, 
    0.0, 1.0, 1.0, 0.0, 
    0.0, 0.0, 1.0, 0.0, 
    0.0, 0.0, 0.0, 1.0, ])

#밤 분위기
transform night_tint:
    matrixcolor TintMatrix("#9d9ec4")

transform red_tint:
    matrixcolor TintMatrix("#ff0000")





