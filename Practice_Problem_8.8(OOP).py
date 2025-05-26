'''

 Implement a class Vector that supports the same methods as the class Point we developed
 in Section8.4.The class Vector should also support vector addition and product operations.
 The addition of two vectors
 v1 = Vector(1, 3)
 v2 = Vector(-2, 4)
 is a new vector whose coordinates are the sum of the corresponding coordinates of v1 and
 v2:
 v1 + v2
 Vector(-1, 7)

'''


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        'initializes point coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        'sets x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'sets y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'returns the x and y coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'changes the x and y coordinates by i and j, respectively'
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point({}, {})'.format(self.x, self.y)


class Vector(Point):
    'class that represents a vector in the plane, extends Point'

    def __add__(self, other):
        'returns a new vector that is the sum of self and other'
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, other):
        'returns the dot product of self and other'
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __repr__(self):
        'return canonical string representation Vector(x, y)'
        return 'Vector({}, {})'.format(self.x, self.y)

v1 = Vector(1, 3)
v2 = Vector(-2, 4)

print(v1 + v2)  # Vector(-1, 7)
print(v1 * v2)  # 10


