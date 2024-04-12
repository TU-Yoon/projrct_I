

init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=[]): #아이템 속성
            self.name = name #아이템 이름
            self.image = image #아이템 이미지
            self.value = int(value) #상점 가격
            self.info = info #아이템 설명
            self.id = id #아이템 코드 문자열
            self.cost = cost 

    ## 인벤토리 기능

        # 항목 추가
        def see(self):
            if self.id not in seen_items:
                seen_items.append(self.id)

        # 레시피 추가
        def see_recipe(self):
            if self.id not in seen_recipes:
                seen_recipes.append(self.id)

        # 항목을 본뒤 인벤토리 추가
        def pickup(self, amount=1):
            self.see()
            while amount>0:
                inv.append(self.id)
                amount -= 1

        # 아이템 삭제
        def toss(self, amount):
            while amount>0:
                inv.remove(self.id)
                amount -= 1

        # 골드와 아이템 교환
        def buy(self, amount):
            global gold

            self.see()

            gold -= self.value*amount
            while amount>0:
                inv.append(self.id)
                amount -=1

        # 물건을 골드와 교환
        def sell(self, amount):
            global gold

            gold += int(self.value*amount/2)
            self.toss(amount)

        # 아이템 제작
        def make(self, amount):

            self.see()

            while amount>0:
                for i in self.cost:
                    inv.remove(i)
                inv.append(self.id)
                made_recipes.append(self.id)
                amount -=1

        #상점 화면
        def check_price(self):
            if self.value <= gold:
                return True
            return False


    
    def set_item(self):

        for i in itemlist:
            if self==i[4]: 
                return i

    #인벤토리 정렬
    def sortbyname(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.name

    def sortbyprice(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.value

    def check_ingredients(craftitem):

        check = 0
        for i in craftitem.cost:
            if inv.count(i) > 0:
                check += 1

        if check == len(craftitem.cost):
            return True

        return False

    # 전투 아이템이 있는지 확인
    def check_inv_for(itemtype):
        for i in itemtype:
            if inv.count(i) > 0:
                return True

##=====================================================================##
# 아이템 정의 구간 입니다.

define item_time_warp_pills = (_("타임머신 알약"), "item01", 8,
    _("스크립트를 건너뛴다"), "item_pill")

define item_spicy_pork_cutlet = (_("매운 돈까스"), "item02", 8,
    _("섭취한 인물은 다음 전투에서(전투 관련 선택지 없이) 무조건 승리한다."), "item_spicy_pork_cutlet")

define item_telepathy = (_("기적이 일어나는 텔레파시.exe"), "item03", 8,
    _("두 인물의 몸이 서로 바뀐다."), "item_telepathy")

define item_bundle_money = (_("돈다발 "), "item04", 8,
    _("특정 인물이 자신의 부탁을 무조건 들어준다."), "item_bundle_money")

define item_cellphone = (_("핸드폰"), "item05", 8,
    _("특정 인물에게 전화를 걸 수 있다."), "item_cellphone")

define item_uncharted_Notes = (_("미지의 노트"), "item06", 8,
    _("숨겨진 새로운 선택지를 발견할 수 있다."), "item_uncharted_Notes")

define item_Justice_Man = (_("도와줘요, 저스티스맨!"), "item07", 8,
    _("이야기에 '저스티스맨'이라는 인물이 등장해 개입하게 된다."), "item_Justice_Man")

define item_Random_machine = (_("랜덤머신"), "item08", 8,
    _("랜덤으로 아이템을 하나 획득"), "item_Random_machine")

define item_mk5000 = (_("초전력 플래시 mk5000"), "item09", 8,
    _("숨겨진 지역을 발견할 수 있다."), "item_mk5000")

define item_sweet_music_box = (_("달콤한 오르골"), "item10", 8,
    _("주위에 있는 모든 이를 잠에 빠뜨린다."), "item_sweet_music_box")


# 제작 관련 아이템
define item_sugar = (_("Sweet Sweet Sugar"), "item sugar", 10,
    _("Double sweet! Made from beets."), "item_sugar",
    ["item_beet", "item_water"])

define item_sucker = (_("Common Sucker"), "item sucker", 13,
    _("Syrup's favorite. Use it to recover HP during battle!"), "item_sucker",
    ["item_sugar", "item_paper"])


##############################################################################

# 아이템 리스트
define itemlist = [
    ##
    item_time_warp_pills,
    item_spicy_pork_cutlet,
    item_telepathy,
    item_bundle_money,
    item_cellphone,
    item_uncharted_Notes,
    item_Justice_Man,
    item_Random_machine,
    item_mk5000,
    item_sweet_music_box
    ]

# 아이템 제작
define allrecipes = [
    ]

# 배틀 아이템
define battle_items = [
    ]


# 아이템 레시피
define recipelists = [ allrecipes, battle_items ]
define recipelist_names = [ _("All"), _("Battle") ]
