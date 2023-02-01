class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


x = int(input('Enter lenght of rectengle :'))
y = int(input('Enter width of rectengle :'))
rctngl = Rectangle(x, y)
z = rctngl.area()
print("Area of Rectengle :", z)
