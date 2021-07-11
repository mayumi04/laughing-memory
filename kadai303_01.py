class Pikatyu:
    def __init__(self, name, physical, attack, defence, speed):
        self.name = name
        self.physical = physical
        self.attack = attack
        self.defence =  defence
        self.speed = speed

    def denkousekka(self):
        skill_damage = 10
        skill_name = '電光石火'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}')
    
    def jyuumannboruto(self):
        skill_damage = 20
        skill_name = '10万ボルト'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}') 
            
    def irontail(self):
        skill_damage = 5
        skill_name = 'アイアンテール'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}')   


class Raotyu(Pikatyu):
    def __init__(self, name, physical, attack, defence, speed):
        super(Raotyu, self).__init__(name, physical, attack, defence, speed)
        self.attack = attack * 2

    def rocketzutuki(self):
        skill_damage = 15
        skill_name = 'ロケット頭突き'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}')

    def kaminaripanch(self):
        skill_damage = 60
        skill_name = 'かみなりパンチ'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}')
    
    def kaminari(self):
        skill_damage = 50
        skill_name = 'かみなり'
        damage = self.attack * skill_damage
        print(f'{self.name}が{skill_name}をした!　ダメージ：{damage}')


pikatyu = Pikatyu('さとしピコチュウ', 500, 10, 20, 30)
pikatyu.denkousekka()
pikatyu.jyuumannboruto()

raotyu = Raotyu('さとしラオチュウ', 800, 10, 20, 30)
raotyu.denkousekka()
raotyu.jyuumannboruto()
raotyu.rocketzutuki()