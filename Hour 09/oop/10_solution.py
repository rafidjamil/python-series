class Car:
    total_car = 0
    def __init__(self, brand,model): 
        self.brand = brand 
        self.__model = model
        Car.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.__model} "
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    
    
    @property
    def model(self):
        return self.__model
    
    
        
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
            return "EV"

class Battery:
    def battery_info(self):
        return "100KWH"
class Engine:
    def engine_info(self):
        return "V8 Engine"
class ElectricCar2(Battery, Engine, Car):
    pass

my_tesla = ElectricCar2("Tesla", "Model S")

print(my_tesla.engine_info())
print(my_tesla.battery_info())
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# my_new_car = Car("FORD", "RAPTOR")
# my_new_car= "City"
# print(my_new_car.model)
