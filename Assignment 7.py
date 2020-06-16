class Animal:
    def __init__(self, name, animal_type, age, sound):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.sound = sound


class Jackel(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)


class Lion(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)


class Koala(Animal):
    def __init__(self, name, animal_type, age, sound):
        super().__init__(name, animal_type, age, sound)


zoo_list = []
zoo_list.append(Jackel('Nick', 'Canine', '3', 'AWWWWOOOooooo'))
zoo_list.append(Lion('Oscar', "Feline", '9', 'ROARRRRR'))
zoo_list.append(Koala('Winifred', 'Marsupial', '7', "GRRRRRRRRR"))

print("Welcome to the Zoo")
while 1 == 1:
    user_resp = input('Would you like to go right, left , center, or exit: ')
    if user_resp == 'right' or user_resp == 'Right':
        print('Hello I am a Koala, My name is', zoo_list[2].name)
        print('I am', zoo_list[2].age, 'years old.')
        print('I am a', zoo_list[2].animal_type, 'and I go', zoo_list[2].sound)
    elif user_resp == 'left' or user_resp == 'Left':
        print('Hello I am a Lion, My name is', zoo_list[1].name)
        print('I am', zoo_list[1].age, 'years old.')
        print('I am a', zoo_list[1].animal_type, 'and I go', zoo_list[1].sound)
    elif user_resp == 'center' or user_resp == 'Center':
        print('Hello I am a Jackel, My name is', zoo_list[0].name)
        print('I am', zoo_list[0].age, 'years old.')
        print('I am a', zoo_list[0].animal_type, 'and I go', zoo_list[0].sound)
    elif user_resp == 'exit' or user_resp == 'Exit':
        break
    else:
        print('Invalid Response')

    user_end = input('Would you like to continue exploring the park or exit: ')
    if user_end == 'exit' or user_end == 'Exit':
        break
    else:
        pass
