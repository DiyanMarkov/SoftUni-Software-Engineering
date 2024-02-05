from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance):
        needed = (self.fuel_consumption + Car.CONDITIONER_ON) * distance

        if needed <= self.fuel_quantity:
            self.fuel_quantity -= needed


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6

    def drive(self, distance):
        needed = (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

        if needed <= self.fuel_quantity:
            self.fuel_quantity -= needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95