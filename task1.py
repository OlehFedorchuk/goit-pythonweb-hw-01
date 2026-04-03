from __future__ import annotations

import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return Car("Ford", "Mustang (US Spec)")

    def create_motorcycle(self) -> Motorcycle:
        return Motorcycle("Harley-Davidson", "Sportster (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return Car("BMW", "3 Series (EU Spec)")

    def create_motorcycle(self) -> Motorcycle:
        return Motorcycle("Ducati", "Monster (EU Spec)")


def main() -> None:
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1: Vehicle = us_factory.create_car()
    vehicle1.start_engine()

    vehicle2: Vehicle = us_factory.create_motorcycle()
    vehicle2.start_engine()

    vehicle3: Vehicle = eu_factory.create_car()
    vehicle3.start_engine()

    vehicle4: Vehicle = eu_factory.create_motorcycle()
    vehicle4.start_engine()


if __name__ == "__main__":
    main()
