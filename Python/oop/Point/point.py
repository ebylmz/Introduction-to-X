# Operator Overloading in Python
# https://www.programiz.com/python-programming/operator-overloading

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5 

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    # less than
    def __lt__(self, other):
        return self.magnitude() < other.magnitude() 

    # less than or equal to
    def __le__(self, other):
        return self.magnitude() <= other.magnitude() 
    
    # equal to
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # not equal to
    def __ne__(self, other):
        return not (self == other)
    
    # greater than 
    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
    # greater than or equal to 
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()