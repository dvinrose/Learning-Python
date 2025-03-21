'''

 Start by defining the class Test and then creating two instances of Test in your interpreter
 shell:

class Test:
    version = 1.02

    a = Test()
    b = Test()

 The class Test has only one attribute, the class variable version that refers to float value
 1.02.

 (a) Draw the namespaces associated with the class and the two objects, the names—if
 any—contained in them, and the value(s) the name(s) refer to.

 (b) Execute these statements and fill in the question marks:

 a.version
 ???

 b.version
 ???

 Test.version
 ???

 Test.version=1.03
 a.version
 ???

 Point.version
 ???

 a.version = 'Latest!!'
 Point.version
 ???

 b.version
 ???

 a.version
 ???

  (c) Draw the state of the namespaces after this execution. Explain why the last three
 expressions evaluate the way they did.

'''


# EXERCISE 1

class Point:
    """Class that represents points in the plane"""

    def setx(self, xcoord):
        """Set x coordinate of point to xcoord"""
        self.x = xcoord

    def sety(self, ycoord):
        """Set y coordinate of point to ycoord"""
        self.y = ycoord

    def get(self):
        """Return a tuple with x and y coordinates of the point"""
        return (self.x, self.y)

    def move(self, dx, dy):
        """Change the x and y coordinates by dx and dy"""
        self.x += dx
        self.y += dy

    def getx(self):
        return(self.x)


point = Point()

point.setx(3)
print(point.getx())

# -------------------------------------


class Test:
    version = 1.02


a = Test()
print(a.version)


b = Test()
print(b.version)


Test.version

Test.version = 1.03
print(a.version)

# ---

Point.version

a.version = 'Latest!!'
Point.version


print(b.version)


print(a.version)

help(Point)