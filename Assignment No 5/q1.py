class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rohan", 20)
s2 = Student("Anish", 22)
s3 = Student("Anil", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)
print(s3.name, s3.age)