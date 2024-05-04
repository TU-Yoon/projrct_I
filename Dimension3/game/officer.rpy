image scg_officer normal:
    im.FactorScale("ch/officer/scg officer normal.png", 1.0)
    yalign 0.0

image scg_officer normal2:
    im.FactorScale("ch/officer/scg officer normal2.png", 1.0)
    yalign 0.0

image scg_officer sick:
    im.FactorScale("ch/officer/scg officer sick.png", 1.0)
    yalign 0.0

image scg_officer sick2:
    im.FactorScale("ch/officer/scg officer sick2.png", 1.0)
    yalign 0.0

image scg_officer sick3:
    im.FactorScale("ch/officer/scg officer sick3.png", 1.0)
    yalign 0.0

image scg_officer silly:
    im.FactorScale("ch/officer/scg officer silly.png", 1.0)
    yalign 0.0

image scg_officer wink:
    im.FactorScale("ch/officer/scg officer wink.png", 1.0)
    yalign 0.0

image scg_officer curious:
    im.FactorScale("ch/officer/scg officer curious.png", 1.0)
    yalign 0.0

image scg_officer shake sick middle:
    im.FactorScale("ch/officer/scg officer sick.png", 1.0)
    parallel:
        xalign 0.5
        yalign 0.0
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

image scg_officer shake curious middle:
    im.FactorScale("ch/officer/scg officer curious.png", 1.0)
    parallel:
        xalign 0.5
        yalign 0.0
        easein 0.1 xalign 0.49
        easeout 0.1 xalign 0.51
        repeat 2

#오른쪽 

image scg_officer normal right:
    im.FactorScale("ch/officer/scg officer normal.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer normal2 right:
    im.FactorScale("ch/officer/scg officer normal2.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer sick right:
    im.FactorScale("ch/officer/scg officer sick.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer sick2 right:
    im.FactorScale("ch/officer/scg officer sick2.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer sick3 right:
    im.FactorScale("ch/officer/scg officer sick3.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer silly right:
    im.FactorScale("ch/officer/scg officer silly.png", 1.0)
    xalign 0.9
    yalign 0.0

image scg_officer wink right:
    im.FactorScale("ch/officer/scg officer wink.png", 1.0)
    xalign 0.9
    yalign 0.0



#왼쪽 

image scg_officer normal left:
    im.FactorScale("ch/officer/scg officer normal.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer normal2 left:
    im.FactorScale("ch/officer/scg officer normal2.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer sick left:
    im.FactorScale("ch/officer/scg officer sick.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer sick2 left:
    im.FactorScale("ch/officer/scg officer sick2.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer sick3 left:
    im.FactorScale("ch/officer/scg officer sick3.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer silly left:
    im.FactorScale("ch/officer/scg officer silly.png", 1.0)
    xalign 0.1
    yalign 0.0

image scg_officer wink left:
    im.FactorScale("ch/officer/scg officer wink.png", 1.0)
    xalign 0.1
    yalign 0.0






#부가효과

image scg_officer normal topin:
    im.FactorScale("ch/officer/scg officer normal.png", 1.0)
    parallel:
        xalign 0.5
        yalign -1.0
        easein 2.5 xalign 0.5 yalign 0.0
        easeout 0.5 yalign 0.0

image scg_officer sick topout:
    im.FactorScale("ch/officer/scg officer sick.png", 1.0)
    parallel:
        xalign 0.5
        yalign 0.0
        easein 0.8 xalign 0.5 yalign -1.0

