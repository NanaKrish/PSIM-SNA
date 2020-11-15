from abc import ABC, abstractmethod
from math import sqrt


class Location:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr(f'({self.x}, {self.y})')

    @staticmethod
    def calculate_distance(loc1, loc2) -> float:
        if isinstance(loc1, Location) and isinstance(loc2, Location):
            return sqrt((loc1.x - loc2.x) ** 2 + (loc1.y - loc2.y) ** 2)
        else:
            raise Exception("Requires 2 location params, to compute the distance b/w them")


class Person:
    def __init__(self, name, age: int, location: Location, health_condition: float = 100.0):
        self.age = age
        self.name = name
        self.location = location
        self.health_condition = health_condition

    def __repr__(self):
        return repr(self.name)


class Disease(ABC):

    def __init__(self, infectivity: float, infection_radius: float, infection_type: str):
        self._infectivity = infectivity
        self._infection_radius = infection_radius
        self._infection_type = infection_type

    @abstractmethod
    def infection_function(self, *args, **kwargs):
        pass
