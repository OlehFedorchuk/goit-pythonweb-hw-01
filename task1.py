from abc import ABC, abstractmethod

class Vehicle:
    def start_engine(self):
        ...

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        ...

    def create_motorcycle(self):
        ...

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

class USVehicleFactory(VehicleFactory):
    def create_car(self):
        return Car("Ford", "Mustang (US Spec)")

    def create_motorcycle(self):
        return Motorcycle("Harley-Davidson", "Sportster (US Spec)")
    


class EUVehicleFactory(VehicleFactory):
    def create_car(self):
        return Car("BMW", "3 Series (EU Spec)")

    def create_motorcycle(self):
        return Motorcycle("Ducati", "Monster (EU Spec)")    

# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car()
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle()
vehicle2.start_engine()

vehicle3 = eu_factory.create_car()
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle()
vehicle4.start_engine()