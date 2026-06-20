class Person:
    def __init__(self):
        self.__salary = 15000

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

p = Person()
p.set_salary(30000)
print(p.get_salary())