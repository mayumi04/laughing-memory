class Player:
    def __init__(self, name:str, level:int, items:list):
        self.__name = name
        self.__level = level
        self.__items = items

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level
    
    @property
    def item(self):
        return self.__items

    def memo(self):
        print(f'player Name: {self.__name}\nlevel: {self.__level}')
        # 持ち物リストからitemを一つずつ取り出す
        for i in self.__items:
            for key, value in i.items():
                print(f'Item[{self.__items.index({key:value})+1}]: {key}  × {value}')


class Item:
    def __init__(self, name:str, count:int):
        self.__name = name
        self.__count = count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count
    
    # itemを持ち物リストに追加する
    def motimono(self, motimonolist = []):
        d = {self.__name:self.__count}
        motimonolist.append(d)
        return motimonolist


kaigara = Item('貝殻', 21)
kaigara.motimono()
wakame = Item('布団代わりのワカメ', 3)
wakame.motimono()
sunglass = Item('サングラス', 1)
sunglass.motimono()
ukiwa = Item('浮き輪', 1)
item = ukiwa.motimono()

player = Player('カリュプソー', 99, item)
player.memo()