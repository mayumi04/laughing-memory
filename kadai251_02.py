class Player:
    def __init__(self, bag):
        self.bag = bag

    def ireru(self, *items):
        # bagを用意する
        motimono = self.bag.getItems()
        # bagにitemを入れる
        for item in items:
            in_item = item.iteminfo()
            motimono.append(in_item)

    def toridasu(self):
        # bagに入っているitemをリストで取り出す
        motimono = self.bag.getItems()
        return motimono

    def eat(self, index:int): 
        motimono = player.toridasu()
        # 食べるitemをリストから選ぶ
        food = motimono[index]
        for k, v in food.items():
            print(f'playerは{k}を2個食べた。')
            v = v - 2
            food = {k:v}
            motimono[index] = food


class Donkey:
    def __init__(self, bag):
        self.bag = bag
    
    def ireru(self, items):
        # bagを用意する
        motimono = self.bag.getItems()
        # bagにitemを入れる
        motimono = items
        return motimono

    def toridasu(self):
        motimono = self.bag.getItems()
        return motimono

    def memo(self):
        print('持ち物')
        itemlist = donkey.toridasu()
        for i in itemlist:
            for key, value in i.items():   
                print(f'{key}:　{value}こ')


class Bag:
    def getItems(self, itemlist=[]):
        return itemlist


class Item:
    def __init__(self, name:str, count:int):
        self.__name = name
        self.__count = count
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def count(self):
        return self.__count

    @count.setter
    def setCount(self, count):
        self.__count = count
    
    def iteminfo(self):
        iteminfo = {self.__name:self.__count} 
        return iteminfo


bag = Bag()
player = Player(bag)
donkey = Donkey(bag)
ringo = Item('リンゴ', 3)
pan = Item('パン', 5)

player.ireru(ringo, pan)
player_motimono = player.toridasu()
donkey.ireru(player_motimono)
donkey.memo()
player.eat(0)
donkey.memo()