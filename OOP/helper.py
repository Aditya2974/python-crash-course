# Understanding fundamentals of Object Oriented Programming in Python : 

class Car:
    total_car = 0
    
    def __init__(self,name,model) -> None:
        self.__name = name
        self.__model = model
        Car.total_car += 1
    
    
    def get_name(self):
        return self.__name
    
    def fuel_type(self):
        return 'Petrol or Diesel'


class ElectricCar(Car):
    def __init__(self, name, model,battery_size) -> None:
        super().__init__(name, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'


class Battery:
    def get_info(self):
        return "Battery is based on Lithium Ion"
    

class CarQ(Battery,ElectricCar,Car):
    pass


# Creating a CarQ object:

my_new_car = CarQ("Tesla", "Model X","100kWh")

print(my_new_car.get_info())
