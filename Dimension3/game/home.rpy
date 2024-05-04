
label My_home1:
    $ st = 1  # st는 일상 모드를 구분하는데 사용합니다.
    $ ret = 1
    pause 0.9
    scene c2-2
    show sg
    show screen action_ui
    show screen stat_overlay zorder 1
    "{color=#00FF00} 일상 모드에 진입하였습니다 {/color}"
    "{color=#00FF00} 왼쪽 상단 스태미너를 확인 할 수 있으며 {/color}"
    "{color=#00FF00} 행동 버튼 클릭 시 대화를 걸거나 스토리를 이어 나갈 수 있습니다 {/color}"
    $ some_condition = False
    "청소를 하기 전에 잠깐 다른 걸 해볼까?"
    if some_condition:
        jump s1
    else:
        jump My_home1

label My_home2:
    $ st = 2  # st는 일상 모드를 구분하는데 사용합니다.
    $ ret = 2
    pause 0.9
    scene c2-2
    show sg
    show screen action_ui
    show screen stat_overlay zorder 1
    "{color=#00FF00} 일상 모드에 진입하였습니다 {/color}"
    "{color=#00FF00} 왼쪽 상단 스태미너를 확인 할 수 있으며 {/color}"
    "{color=#00FF00} 행동 버튼 클릭 시 대화를 걸거나 스토리를 이어 나갈 수 있습니다 {/color}"
    $ some_condition = False
    "리스도 깨웠고.. 잠깐 시간이 남을 거 같네"
    if some_condition:
        jump s1
    else:
        jump My_home2

label My_home3:
    $ st = 3  # st는 일상 모드를 구분하는데 사용합니다.
    $ ret = 3
    pause 0.9
    scene c2-2
    show sg
    show screen action_ui
    show screen stat_overlay zorder 1
    "{color=#00FF00} 일상 모드에 진입하였습니다 {/color}"
    "{color=#00FF00} 왼쪽 상단 스태미너를 확인 할 수 있으며 {/color}"
    "{color=#00FF00} 행동 버튼 클릭 시 대화를 걸거나 스토리를 이어 나갈 수 있습니다 {/color}"
    $ some_condition = False
    "설거지도 다 끝냈으니.. 이제 뭘 하지?"
    if some_condition:
        jump s1
    else:
        jump My_home3