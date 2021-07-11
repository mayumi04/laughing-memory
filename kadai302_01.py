class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

class Horse(Animal):
    def __init__(self, name, weight, speed):
        super(Horse, self).__init__(name, weight)
        self.speed = speed
    
    def get_speed(self):
        return self.speed
        
    def run (self):
        name = horse.get_name()
        speed = horse.get_speed()
        print(f'{name}走る。(速度：{speed}km/h)')

    def run_with_jockey(self, jockey_weight):
        # 乗馬者の全体重を出す
        all_weight = jockey_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - jockey_weight/20
            name = horse.get_name()
            return print(f'{name}走る。乗馬者1名　(速度：{speed}km/h)')

    def run_with_person(self, *args):
        # 乗馬者のうち人の全体重を出す
        person_weight = sum(args)
        # 乗馬者の全体重を出す 
        all_weight = person_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - person_weight/10
            name = horse.get_name()
            # 乗馬者の人数を数える
            person_count = len(args)
            return print(f'{name}走る。乗馬者{person_count}名　(速度：{speed}km/h)')
            
    def run_with_jockey_person(self, jockey_weight, *args):
        # 乗馬者のうち人の全体重を出す
        person_weight = sum(args)
        # 乗馬者の全体重を出す 
        all_weight = jockey_weight + person_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - jockey_weight/20 - person_weight/10
            name = horse.get_name()
            # 乗馬者の人数を数える　騎手１名＋人の人数
            person_count = 1 + len(args)
            return print(f'{name}走る。乗馬者{person_count}名　(速度：{speed}km/h)')


class Jockey(Animal):
    pass


class Person(Animal):
    pass

    
horse = Horse('ディープインパクト', 200.5, 50)
jockey = Jockey('武 豊', 50.2)
person = Person('田中', 70.2)
person2 = Person('佐藤', 60.6)

horse_name = horse.get_name()
horse_weight = horse.get_weight()
horse_speed = horse.get_speed()
print(f'{horse_name}　(体重：{horse_weight}kg, 速度：{horse_speed}km/h)')

jockey_name = jockey.get_name()
jockey_weight = jockey.get_weight()
print(f'{jockey_name}　(体重：{jockey_weight}kg)')

person_name = person.get_name()
person_weight = person.get_weight()
print(f'{person_name}　(体重：{person_weight}kg)')

person2_name = person2.get_name()
person2_weight = person2.get_weight()
print(f'{person2_name}　(体重：{person2_weight}kg)')

horse.run()
horse.run_with_person(person_weight, person2_weight)
horse.run_with_jockey(jockey_weight)
horse.run_with_jockey_person(jockey_weight, person_weight, person2_weight)
