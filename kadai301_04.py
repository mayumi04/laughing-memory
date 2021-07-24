class Person:
    def __init__(self, name, weight, pet):
        self.name = name
        self.weight = weight
        self.pet = pet

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight
    
    def set_pet_name(self, name):
        return self.pet.changename(name)
        
    def set_pet_weight(self, weight):
        return self.pet.changeweight(weight)


class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def changename(self, name):
        self.name = name
        return self.name

    def changeweight(self, weight):
        self.weight = weight
        return self.weight


tarotaro = Pet('犬', 1)
taro = Person('たろ', 100.3, tarotaro)
name = taro.get_name()
weight = taro.get_weight()
pet_name = taro.set_pet_name('たろたろ')
pet_weight = taro.set_pet_weight(10.2)
print(f'飼い主：{name}　{weight}kg　ペット：{pet_name}　{pet_weight}kg')

jirojiro = Pet('犬', 1)
jiro = Person('じろ', 70.5, jirojiro)
name = jiro.get_name()
weight = jiro.get_weight()
pet_name = jiro.set_pet_name('じろじろ')
pet_weight = jiro.set_pet_weight(30.2)
print(f'飼い主：{name}　{weight}kg　ペット：{pet_name}　{pet_weight}kg')