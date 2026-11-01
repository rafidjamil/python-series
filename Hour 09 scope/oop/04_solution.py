# Encapsulation
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def fullname(self):
        return f"{self.brand} {self.model}"


my_tesla = Car("Tesla", "S2")
print(my_tesla.get_brand())
