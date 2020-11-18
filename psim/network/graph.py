import networkx as nx

from psim.agents.entity import Population


class InfectionGraph:

    def __init__(self, population: Population):
        self.__population = population
        self.__graph = self.__construct_initial_graph()

    def __construct_initial_graph(self) -> nx.DiGraph:
        """
        Initializes the infection graph
        """
        pass

