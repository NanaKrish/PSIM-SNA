from abc import ABC, abstractmethod
from copy import deepcopy

import numpy as np


def enable_cem(func):
    def wrapper(*args, **kwargs):
        print("Enabler called")
        BaseCEM.states.append(deepcopy(args))
        BaseCEM.enforcement_key_stack.append(args)
        return func(*args, **kwargs)

    return wrapper


def disable_cem(func):
    def wrapper(*args):
        print("Disabler called")
        values = BaseCEM.states.pop()
        keys = BaseCEM.enforcement_key_stack.pop()
        keys = values
        return keys

    return wrapper


class BaseCEM(ABC):
    """
    Base interface for Counter Effective Methods (CEM)
    """

    def __init__(self, key):
        self.enforcement_key = key

    @abstractmethod
    def activate_enforcement(self, *args):
        pass

    @abstractmethod
    def relax_enforcement(self, *args):
        pass


class SocialDistancing(BaseCEM):
    """
    CEM described in this class increases the distance b/w the population, i.e. decreasing interaction.
    """
    def __init__(self, distance_matrix: np.ndarray):
        super().__init__(distance_matrix)

    @staticmethod
    @enable_cem
    def activate_enforcement(distance_matrix: np.ndarray, safe_distance: float = None):
        print("Social Distance enforcement")
        if safe_distance is None:
            safe_distance = distance_matrix.mean()
        for i, row in enumerate(distance_matrix):
            for j, val in enumerate(row):
                distance_matrix[i][j] += np.random.randint(val,
                                                           int(val + safe_distance)) if 0 < val < safe_distance else val
        return distance_matrix

    @staticmethod
    @disable_cem
    def relax_enforcement(distance_matrix: np.ndarray):
        print("Social Distance enforcement uplifted")
