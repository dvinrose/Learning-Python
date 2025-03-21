'''

 Implement class Rectangle that represents rectangles. The class should support methods:
 • setSize(width, length): Takes two number values as input and sets the length
 and the width of the rectangle
 • perimeter(): Returns the perimeter of the rectangle
 • area(): Returns the area of the rectangle

 rectangle = Rectangle(3,4)

 rectangle.perimeter()
 14

 rectangle.area()
 12

'''

class Rectangle:

    def setSize(self,width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        return 2*(self.width + self.length)
    def area(self):
        return self.width * self.length

rectangle = Rectangle()

rectangle.setSize(3,4)
print(rectangle.perimeter())
print(rectangle.area())
