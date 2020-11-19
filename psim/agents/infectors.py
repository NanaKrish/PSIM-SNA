from psim.agents.entity import Disease, Population
from random import choice


class COVID19(Disease):
    def __init__(self, infectivity: float, infection_radius: float, infection_type: str):
        super().__init__(infectivity, infection_radius, infection_type)

    def infection_function(self, population: Population):
        g = population.get_graph()
        # TODO: Do what we need to do for the 
        # infection to spread
        u = choice(list(g.nodes()))
        population.infect_person(u)
