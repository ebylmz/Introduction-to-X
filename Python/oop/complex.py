class Complex:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print(f"{self.real} + {self.imag}i")
    
c1 = Complex(1)
c1.getData()

c2 = Complex(5, 7)
# create a new attribute 'attr'
# attribute only for object not class so c1 object does not have attribute 'attr'
c2.attr = 10    
print(c2.real, c2.imag, c2.attr)

# Any attribute of an object can be deleted anytime
del c1.imag
# after delating attribute 'imag' method getData() become invalid for c1
# We can even delete the object itself, using the del statement.

# Deleting objects in Python just removes the name binding
# Later automaticly destroyed by the garbage collector
del c1