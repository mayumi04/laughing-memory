class Cow:
    def __init__(self, name:str, age:int, gender:bool, weight:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def talk(self):
        if self.gender:
            gender_name = 'メス'
        else:
            gender_name = 'オス'
        print(f'{self.name} {self.age}歳 {gender_name} {self.weight}kg')


hanako = Cow('はなこ', 3, True, 100.4)
tarou = Cow('たろう', 4, False, 200.5)
mugen = Cow('むげん', 9, False, 300.6)

hanako.talk()
tarou.talk()
mugen.talk()