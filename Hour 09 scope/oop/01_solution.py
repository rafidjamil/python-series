class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fullname(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())


my_car = Car("BMW", "M5")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())

