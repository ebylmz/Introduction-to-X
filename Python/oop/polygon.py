class Polygon:
    def __init__(self, n):
        self.n = n  # number of side
        self.sides = [0 for _ in range(n)]
    
    def inputSides(self):
        self.sides = [float(input(f"Side {i + 1}: ")) for i in range(self.n)]
    
    def displaySides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")

class Triangle(Polygon):
    def __init__(self):
        # call super class constructor
        super().__init__(3) # equivalent to Polygon.__init__(self, 3) 

    def findArea(self):
        a, b, c = self.sides

        # calculate semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of the triangle is %0.2f" % area)

    def isRightTriangle(self):
        # has one angle 90 degree
        a, b, c = sorted(self.sides)
        return a**2 + b**2 == c**2 

t = Triangle()
t.inputSides()
t.displaySides()
t.findArea()
print(f"Right Triangle: {t.isRightTriangle()}")

print(f"issubclass(bool, int): {issubclass(bool, int)}") # true
print(f"issubclass(Triangle, Polygon): {issubclass(Triangle, Polygon)}") # true
print(f"isinstance(t, Triangle): {isinstance(t, Triangle)}") # true
print(f"isinstance(t, Polygon): {isinstance(t, Polygon)}") # true

# all the classes derived from object class like Java does
print(f"issubclass(Triangle, object): {issubclass(Triangle, object)}") # true
print(f"isinstance('Hello', object): {isinstance('Hello', object)}") # true
print(f"isinstance(5.5, object): {isinstance(5.5, object)}") # true
