# Inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
class ElectricCar(Car):
        def __init__(self, brand, model, battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size
        def fuel_type(self):
            return "Electric charge"

my_tesla = ElectricCar("Tesla", "S2", "800KWH")
my_car = Car("Toyota", "Corolla")
print(my_car.brand,my_car.fuel_type())
print(my_tesla.brand,my_tesla.fuel_type())
