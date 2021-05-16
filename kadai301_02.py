class Cow:
    def __init__(self, name:str, age:int, gender:bool, weight:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

        if gender:
            self.gender = 'メス'
        else:
            self.gender = 'オス'

    def talk(self):
        print(f'{self.name} {self.age}歳 {self.gender} {self.weight}kg')


hanako = Cow('はなこ', 3, 1, 100.4)
tarou = Cow('たろう', 4, 0, 200.5)
mugen = Cow('むげん', 9, 0, 300.6)

hanako.talk()
tarou.talk()
mugen.talk()