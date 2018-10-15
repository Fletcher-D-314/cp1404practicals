from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(1, 100) < self.reliability:
            distance_driven = super().drive(distance)

        else:
            distance_driven = 0
        return distance_driven
