from collections import defaultdict

from psim.agents.cem import BaseCEM
from psim.agents.entity import Disease, Population
from random import choice

class PSIMModel:
    def __init__(self, population: Population, disease: Disease):
        self.population = population
        self.disease = disease
        self.cems = defaultdict(list)
        # Randomly infect a person first
        u = choice(self.population.get_people())
        u.healthy = False
        print('Infected with virus:', u)

    def register_cem(self, target_week: int, cem: BaseCEM):
        self.cems[target_week].append(cem)

    def simulate_one_step(self):
        g = self.population.get_graph()
        # TODO: Do what we need to do for the 
        # infection to spread
        u = choice(list(g.nodes()))
        u.healthy = False

    def simulate(self):
        pass
