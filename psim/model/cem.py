from abc import ABC, abstractmethod


class BaseCEM(ABC):
    """
    Base interface for Counter Effective Methods (CEM)
    """

    @abstractmethod
    def reduce_infection(self, *args, **kwargs):
        pass
