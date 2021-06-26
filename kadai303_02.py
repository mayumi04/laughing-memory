from abc import ABCMeta, abstractmethod


class Controller(metaclass=ABCMeta):
    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass


class Game():
    def __init__(self, title, charactar):
        self.title = title
        self.charactar = charactar

    def start(self):
        print(f'{self.title}スタート')


class Dorakoe(Controller, Game):
    def up(self):
        print(f'上　{self.charactar}が上に進む')

    def down(self):
        print(f'下　{self.charactar}が下に進む')
    
    def left(self):
        print(f'左　{self.charactar}が左に進む')

    def right(self):
        print(f'右　{self.charactar}が右に進む')


class Streetfighter(Controller, Game):
    def up(self):
        print(f'上　{self.charactar}がジャンプする')

    def down(self):
        print(f'下　{self.charactar}がしゃがむ')
    
    def left(self):
        print(f'左　{self.charactar}が後に進む')

    def right(self):
        print(f'右　{self.charactar}が前に進む')


dorakoe = Dorakoe('ドラコエ', '勇者')
dorakoe.start()
dorakoe.up()
dorakoe.down()
dorakoe.left()
dorakoe.right()

streetfighter = Streetfighter('ストリートフォイター', '春香')
streetfighter.start()
streetfighter.up()
streetfighter.down()
streetfighter.left()
streetfighter.right()
