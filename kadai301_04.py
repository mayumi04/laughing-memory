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
        self.pet.changename(name)

    def set_pet_weight(self, weight):
        self.pet.changeweight(weight)


class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def changename(self, name):
        self.name = name

    def changeweight(self, weight):
        self.weight = weight

    def get_name(self):
        return self.name
        
    def get_weight(self):
        return self.weight


dog = Pet('犬', 3)

person = Person('たろ', 100.3, dog)
person.set_pet_name('たろたろ')
person.set_pet_weight(10.2)
name = person.get_name()
weight = person.get_weight()
pet_name = dog.get_name()
pet_weight = dog.get_weight()
print(f'飼い主：{name}　{weight}kg　ペット：{pet_name}　{pet_weight}kg')

person = Person('じろ', 70.5, dog)
person.set_pet_name('じろじろ')
person.set_pet_weight(30.2)
name = person.get_name()
weight = person.get_weight()
pet_name = dog.get_name()
pet_weight = dog.get_weight()
print(f'飼い主：{name}　{weight}kg　ペット：{pet_name}　{pet_weight}kg')