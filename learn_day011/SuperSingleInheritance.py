class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        ar = super().area()
        print("Area of Square :: ", ar)
        return ar


sqr = Square(4)
print("Area of Square is:", sqr.area())

rect = Rectangle(2, 4)
print("Area of Rectangle is:", rect.area())
