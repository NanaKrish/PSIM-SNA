from abc import ABC, abstractmethod

import numpy as np


class BaseCEM(ABC):
    """
    Base interface for Counter Effective Methods (CEM)
    """

    @abstractmethod
    def reduce_infection_rate(self, *args):
        pass

    def relax_enforcement(self):
        # TODO: Load pre enforcement state
        pass


class SocialDistancing(BaseCEM):
    """
    CEM described in this class increases the distance b/w the population, i.e. decreasing interaction.
    """

    @staticmethod
    def reduce_infection_rate(distance_matrix: np.ndarray, safe_distance: float = None):
        if safe_distance is None:
            safe_distance = distance_matrix.mean()
        matrix = np.zeros(distance_matrix.shape)
        for i, row in enumerate(distance_matrix):
            for j, val in enumerate(row):
                matrix[i][j] += np.random.randint(val, int(val + safe_distance)) if 0 < val < safe_distance else val
        return matrix
