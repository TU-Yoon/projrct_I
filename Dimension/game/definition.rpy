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

define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 1.5)
define left2 = Position(xalign = 0.1)



image scg_reese:
    im.FactorScale("ch/reese/scg reese test.png", 1.0)
    yalign 0.0

# 리스 평상 시 -> scg_reese normal
image scg_reese normal:
    im.FactorScale("ch/reese/scg reese normal.png", 1.0)
    yalign 0.0

# 리스 평상 시 걸을 때 -> scg_reese normal walk
image scg_reese normal walk:
    im.FactorScale("ch/reese/scg reese normal.png", 1.0)
    parallel:
        yalign 0.0
        easeout 1.5 yalign -0.1
        easeout 1.0 yalign 0.0
        repeat

# 리스가 화날 때 -> scg_reese angry
image scg_reese angry:
    im.FactorScale("ch/reese/scg reese angry.png", 1.0)
    yalign 0.0

# 리스가 웃을 때 -> scg_reese smile
image scg_reese smile:
    im.FactorScale("ch/reese/scg reese smile.png", 1.0)
    yalign 0.0

# 리스가 행복할 때 -> scg_reese happy
image scg_reese happy:
    im.FactorScale("ch/reese/scg reese happy.png", 1.0)
    yalign 0.0

# 리스가 황당할 때 -> scg_reese confuse
image scg_reese confuse:
    im.FactorScale("ch/reese/scg reese confuse.png", 1.0)
    yalign 0.0

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('매시안', color="#0bb9d8")
define r = Character('리스', color="#ff0000")
define n = Character('노웰', color="#00ff04")
define mys = Character('???', color="#1f1f1f")
define scala = Character('스칼라', color="#84860f")
define 연구원 = Character('연구원', color="#1f1f1f")
define d = Character('디멘트리', color="#1f1f1f")

# 독백은 ch_na로 고정(na는 형식상 존재)
define na = Character(None, kind = nvl)
define ch_na = Character(None)


#기타 인물 - 프롤로그
define fish = Character('생선 아줌마', color="#000000")
define bus = Character('버스 기사', color="#000000")
define del = Character('배달원', color="#000000")



## 효과 코드

#Fade(지속시간, 시작할 때의 투명도, 끝날 때의 투명도, color=색상)
#flash = 반짝이는 연출
define flash = Fade(2, 0, .75, color="#fff")

#eclipsy = 깜빡이는 연출
define eclipsy = Fade(0.01, 0, 1, color="#ddf4ff")

# eyeclose = 눈이 감기는 연출
define eyeclose = Fade(3, 0, 1, color="#000000")

# eyecloseslow = 눈이 천천히 감기는 연출(추가)
define eyecloseslow = Fade(3, 1.5, 1, color="#000000")


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

#

