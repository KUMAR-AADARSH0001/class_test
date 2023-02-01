class Circle():
    def __init__(self, radius):
        self.r = radius

    def area(self, r):
        area = 3.14*r**2
        print("Area of the circle is: ", area)

    def perameter(self, r):
        pera = 2*3.14*r
        print("Perimeter of the circle is: ", pera)


x = int(input('Enter Radius of Circle :'))
c = Circle(x)
c.area(x)
c.perameter(x)
