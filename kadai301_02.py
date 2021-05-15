class Cow():
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def talk(self):
        print(f'{self.name} {self.age}歳 {self.gender} {self.weight}kg')

hanako = Cow('はなこ', 3, 'メス', 100.4)
tarou = Cow('たろう', 4, 'オス', 200.5)
mugen = Cow('むげん', 9, 'オス', 300.6)
hanako.talk()
tarou.talk()
mugen.talk()