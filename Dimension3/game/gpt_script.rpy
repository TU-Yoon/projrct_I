define e = Character("리스")
define d = Character("메시안")
define proxy = "http://dasffvsd.kro.kr/proxy.php"

label chatgptmode:
scene c2-2
show scg_reese1
show screen stat_overlay
show screen action_ui

python:
    import chatgpt
    from chatgpt.messages_data import get_messages
    messages = get_messages()
    while True:
        renpy.hide("scg_reese1")
        renpy.show("scg_reese1")
        user_input = renpy.input("무슨말을 할까?", length=1000)
        messages.append({"role": "user", "content": user_input})
        messages = chatgpt.completion(messages, proxy=proxy)
        response = messages[-1]["content"]

        renpy.say(d, user_input)

        if response[0] == '1':
            persistent.sit[1] -= 1
        elif response[0] == '3':
            persistent.sit[1] += 1
    
        modified_response = response[1:]
    
        e(modified_response)
        if response[0] == '3':
            renpy.hide("scg_reese1")
            renpy.show("scg_reese1 happy")
            e("리스의 기분이 좋아진 것 같다. {color=#00FF00}(친밀도가 1 상승 하였습니다){/color}")
            if persistent.sit[0] >= 20:
                persistent.sit[0] -= 20
            else:
                e("기운이 부족하여 더 이상 말을 걸 수 없을 것 같다. {color=#00FF00}(대화를 마칩니다.){/color}")
                renpy.jump("My_home")
        elif response[0] == '1':
            renpy.hide("scg_reese1")
            renpy.show("scg_reese1 silly")
            e("리스의 기분이 나빠진 것 같다. {color=#F05650}(친밀도가 1 하락 하였습니다){/color}")
            if persistent.sit[0] >= 20:
                persistent.sit[0] -= 20
            else:
                e("기운이 부족하여 더 이상 말을 걸 수 없을 것 같다. {color=#00FF00}(대화를 마칩니다.){/color}")
                renpy.jump("My_home")
        else:
            e("(평범한 대화였던 것 같다)")
            if persistent.sit[0] >= 20:
                persistent.sit[0] -= 20
            else:
                e("기운이 부족하여 더 이상 말을 걸 수 없을 것 같다. {color=#00FF00}(대화를 마칩니다.){/color}")
                renpy.jump("My_home")


    # while True:
    #     user_input = renpy.input("무슨말을 할까?", length=1000)
    #     messages.append(
    #         {"role": "user", "content": user_input}
    #     )
    #     messages = chatgpt.completion(messages,proxy=proxy)
    #     response = messages[-1]["content"]
    #     e("[response]")
    #     e("리스의 기분이 좋아진 것 같다. {color=#00FF00}(친밀도가 1 상승 하였습니다){/color}")
    #     persistent.sit[1] += 1

