class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Lion(Animal):
    def make_sound(self):
        print("Roar")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


animals = [Dog(), Lion(), Cat()]

for animal in animals:
    animal.make_sound()