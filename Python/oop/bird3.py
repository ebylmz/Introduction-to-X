# Polymorphism in Python

class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot cannot swim")

class Penguin:
    def fly(self):
        print("Penguin cannot fly")
    
    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)