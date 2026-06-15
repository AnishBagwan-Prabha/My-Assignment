class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand, self.price)

m = Mobile("Oppo", 20000)
m.show()