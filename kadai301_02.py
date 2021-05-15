class Cow():
    def talk(self, name, age, gender, weight):
        print(f'{name} {age}歳 {gender} {weight}kg')

cow = Cow()
cow.talk('はなこ', 3, 'メス', 100.4)
cow.talk('たろう', 4, 'オス', 200.5)
cow.talk('むげん', 9, 'オス', 300.6)