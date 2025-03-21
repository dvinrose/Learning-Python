'''

Add method getx() to the class Point; this method takes no input and returns the x coor
dinate of the Point object invoking the method.

a.getx()

 3

'''

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