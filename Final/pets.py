class Animal:
    def __init__(self, name, age, breed, animal_type):
        self.name = name
        self.age = age
        self.breed = breed
        self.animal_type = animal_type
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return self.commands

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Breed: {self.breed}, Type: {self.animal_type}"

class DomesticAnimal(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed, "Domestic Animal")

class PackAnimal(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed, "Pack Animal")

class Dog(DomesticAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

class Cat(DomesticAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

class Hamster(DomesticAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

class Horse(PackAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

class Camel(PackAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

class Donkey(PackAnimal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
