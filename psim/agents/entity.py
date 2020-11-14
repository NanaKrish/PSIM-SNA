from abc import ABC, abstractmethod


class Location:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr(f'({self.x}, {self.y})')

    @staticmethod
    def calculate_distance(loc1, loc2) -> float:
        if isinstance(loc1, Location) and isinstance(loc2, Location):
            # TODO: Implement distance b/w 2 points algo
            pass
        else:
            raise Exception("Requires 2 location params, to compute the distance b/w them")


class Person:
    def __init__(self, name, age: int, location: Location):
        self.age = age
        self.name = name
        self.location = location

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