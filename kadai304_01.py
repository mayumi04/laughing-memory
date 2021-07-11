class Fish:
    def __init__(self, name='魚'):
        self.name = name

    def swim(self):
        print(f'{self.name}は泳ぐ。')


class Demekin(Fish):
    def __init__(self, name='出目金'):
        super(Demekin, self).__init__(name)

    def swim(self):
        print(f'{self.name}はふりふり泳ぐ。')


class Same(Fish):
    def __init__(self, name='サメ'):
        super(Same, self).__init__(name)

    def swim(self):
        print(f'{self.name}はすいすい泳ぐ。')


class Sirakansu(Fish):
    def __init__(self, name='シーラカンス'):
        super(Sirakansu, self).__init__(name)

    def swim(self):
        print(f'{self.name}はゆらゆら泳ぐ。')


fish = Fish()
fish.swim()

demekin = Demekin()
demekin.swim()

same = Same()
same.swim()

sirakansu = Sirakansu()
sirakansu.swim()