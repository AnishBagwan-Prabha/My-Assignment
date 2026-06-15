class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Anish")
print(s.name)