class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(self.brand, self.model)

c1 = Car("Tata", "Nexon")
c1.show()