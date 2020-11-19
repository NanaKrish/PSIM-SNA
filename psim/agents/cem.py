from abc import ABC, abstractmethod

import networkx as nx


class BaseCEM(ABC):
    """
    Base interface for Counter Effective Methods (CEM)
    """

    @abstractmethod
    def enforce(self, *args):
        pass

    @abstractmethod
    def relax_enforcement(self):
        pass


class SocialDistancing(BaseCEM):
    """
    CEM described in this class increases the distance b/w the population, i.e. decreasing interaction.
    """

    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.count = 0

    def enforce(self):
        self.count += 1
        for edge in self.graph.edges(data=True):
            weight = edge[2]['weight']
            edge[2]['weight'] = weight - weight * 0.23
        print(f"\nSocial Distancing - {self.count} enforced")

    def relax_enforcement(self):
        for edge in self.graph.edges(data=True):
            weight = edge[2]['weight']
            edge[2]['weight'] = weight + weight * 0.23
        print(f"\nSocial Distancing - {self.count} relaxed")
