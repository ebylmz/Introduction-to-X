class Parrot:
    # class attribute
    species = "bird"

    # instance attribute (Constructor)
    def __init__(self, name, age):
        # single or double underscore prefix denotes private attributes 
        self.name = name
        self.age = age

    # whenever an object calls its method, the object itself is passed
    # as the first argument. So, blue.sing() translates into Parrot.sing(harry).

    # instance method
    def sing(self, song):
        return f"{self.name} sings {song}"
    
    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the Parrot Class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print(f"Blu is a {blu.__class__.species}")
print(f"Woo is also a {woo.__class__.species}")

# access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")

# call our instance methods
print(blu.sing("happy"))
