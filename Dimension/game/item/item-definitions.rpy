

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

define item_pill = (_("알약"), "item pill", 3,
    _("타임 워프를 할 수 있는 알약이다."), "item_pill")


##############################################################################

# 아이템 리스트
define itemlist = [
    item_pill,
    ]

# 아이템 제작
define allrecipes = [
    "item_sugar",
    "item_sucker"
    ]

# 배틀 아이템
define battle_items = [
    "item_ka"
    ]


# 아이템 레시피
define recipelists = [ allrecipes, battle_items ]
define recipelist_names = [ _("All"), _("Battle") ]
