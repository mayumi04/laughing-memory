class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def memo(self):
        print(f'{self.name}　(体重：{self.weight}kg)')


class Horse(Animal):
    def __init__(self, name, weight, speed):
        super(Horse, self).__init__(name, weight)
        self.speed = speed

    def get_speed(self):
        return self.speed

    def memo(self):
            print(f'{self.name}　(体重：{self.weight}kg, 速度：{self.speed}km/h)')
        
    def run (self):
        name = horse.get_name()
        speed = horse.get_speed()
        print(f'{name}走る。(速度：{speed}km/h)')

    def run_with_jockey(self, jockey):
        jockey_weight = jockey.get_weight()
        # 乗馬者の全体重を出す
        all_weight = jockey_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - jockey_weight/20
            name = horse.get_name()
            return print(f'{name}走る。乗馬者1名　(速度：{speed}km/h)')

    def run_with_person(self, *persons):
        # 乗馬者のうち人の全体重を出す
        person_weight = 0
        for person in persons:    
            person_weight += person.get_weight()
        # 乗馬者の全体重を出す 
        all_weight = person_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - person_weight/10
            name = horse.get_name()
            # 乗馬者の人数を数える
            person_count = len(persons)
            return print(f'{name}走る。乗馬者{person_count}名　(速度：{speed}km/h)')
            
    def run_with_jockey_person(self, jockey_weight, *persons):
        jockey_weight = jockey.get_weight()
        # 乗馬者のうち人の全体重を出す
        person_weight = 0
        for person in persons:    
            person_weight += person.get_weight()
        # 乗馬者の全体重を出す 
        all_weight = jockey_weight + person_weight
        # 乗馬者の全体重が200kgを超えると馬は走れない
        if all_weight>200:
            print('重くて走れないよ')
        else:
            speed = self.speed - jockey_weight/20 - person_weight/10
            name = horse.get_name()
            # 乗馬者の人数を数える　騎手１名＋人の人数
            person_count = 1 + len(persons)
            return print(f'{name}走る。乗馬者{person_count}名　(速度：{speed}km/h)')


class Jockey(Animal):
    pass


class Person(Animal):
    pass

    
jockey = Jockey('武 豊', 50.2)
person = Person('田中', 70.2)
person2 = Person('佐藤', 60.6)
horse = Horse('ディープインパクト', 200.5, 50)

horse.memo()
jockey.memo()
person.memo()
person2.memo()

horse.run()
horse.run_with_person(person, person2)
horse.run_with_jockey(jockey)
horse.run_with_jockey_person(jockey, person, person2)