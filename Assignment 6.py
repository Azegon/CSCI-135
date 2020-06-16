class Animal:
    def __init__(self, name, animal_type, age, sound):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.sound = sound

class Jackel(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)

    def info(self):
          print('Hello I\'m a Jackel, My name is %.\nI am % years old.\nI am a %, and I go %.' % (self.name, self.age, self.animal_type, self.sound))

class Lion(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)

    def info(self):
          print('Hello I\'m a Lion, My name is %.\nI am % years old.\nI am a %, and I go %.' % (self.name, self.age, self.animal_type, self.sound))

class Koala(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)

    def info(self):
          print('Hello I\'m a Koala, My name is %.\nI am % years old.\nI am a %, and I go %.' % (self.name, self.age, self.animal_type, self.sound))

zoo_jackel = Jackel('Nick', 'Canine', '3', 'AWWWWOOOooooo')
zoo_lion = Lion('Oscar', "Feline", '9', 'ROARRRRR')
zoo_koala = Koala('Winifred', 'Marsupial', '7', "GRRRRRRRRR")
print(zoo_jackel.name, zoo_jackel.animal_type, zoo_jackel.age, zoo_jackel.sound)
print(zoo_lion.name, zoo_lion.animal_type, zoo_lion.age, zoo_lion.sound)
print(zoo_koala.name, zoo_koala.animal_type, zoo_koala.age, zoo_koala.sound)

