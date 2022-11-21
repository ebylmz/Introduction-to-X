# Encapsulation in Python
class Computer:
    def __init__(self, maxprice):
        # single or double underscore prefix denotes private attributes 
        self.__maxprice = maxprice
    
    def sell(self):
        print(f"Selling Price {self.__maxprice}")
    
    def setMaxPrice(self, price):
        self.__maxprice = price if price > 0 else 0
    
    def getMaxPrice(self):
        return self.__maxprice

c = Computer(1000)
c.sell()


c.__maxprice = 2000 # does not change object attribute
print(c.__maxprice)  # prints 2000
c.sell()

c.setMaxPrice(3000)
c.sell()