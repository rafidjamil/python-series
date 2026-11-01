# Inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
class ElectricCar(Car):
        def __init__(self, brand, model, battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "S2", "800KWH")
print(my_tesla.fullname(),my_tesla.battery_size)
