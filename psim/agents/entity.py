from abc import ABC, abstractmethod
from math import sqrt
from typing import List, Generator, Any

import numpy as np


class Disease(ABC):
    def __init__(self, infectivity: float, infection_radius: float, infection_type: str):
        self._infectivity = infectivity
        self._infection_radius = infection_radius
        self._infection_type = infection_type

    @abstractmethod
    def infection_function(self, *args):
        pass


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
            raise Exception(
                f"Requires 2 location params, to compute the distance b/w them. Got {type(loc1)} & {type(loc2)}"
            )

    @staticmethod
    def calculate_distance_matrix(population) -> np.ndarray:
        if not isinstance(population, Population):
            raise Exception(f"Expected population as param got {type(population)}")
        matrix = np.zeros((population.size(), population.size()))

        for i, p1 in enumerate(population.get_people()):
            for j, p2 in enumerate(population.get_people()):
                if i < j:
                    matrix[i][j] = Location.calculate_distance(p1.location, p2.location)
        return matrix


class Person:
    def __init__(self, name: str, age: int, location: Location, healthy: bool = True):
        self.name = name
        self.age = age
        self.location = location
        self.healthy = healthy

    def __repr__(self):
        return repr(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


class Population:
    def __init__(self, data: Generator[Person, None, Any]):
        self.__population = self.__construct_population(data)

    @staticmethod
    def __construct_population(data: Generator[Person, None, Any]):
        """General Note: This method can be optimised later if required to reduce memory usage for large datasets"""
        return [x for x in data]

    def get_people(self) -> List[Person]:
        return self.__population

    def size(self):
        return len(self.__population)

    def get_population_status(self, raw=False):
        """
        Returns the health status of the population
        :param raw: If True, returns dict of people grouped into healthy and infected
        """
        if raw:
            status = {
                "healthy": [],
                "infected": [],
            }
        else:
            status = {
                "healthy": 0,
                "infected": 0,
            }
        for person in self.get_people():
            key = "healthy" if person.healthy else "infected"
            if raw:
                status[key].append(person)
            else:
                status[key] += 1
        return status
