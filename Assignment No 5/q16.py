class Shape:
    def area(self):
        pass

class Circle(Shape):
    def _init_(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def _init_(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

print("Circle Area:", Circle(7).area())
print("Rectangle Area:", Rectangle(8, 5).area())