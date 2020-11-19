from collections import defaultdict
from random import choice

from psim.agents.cem import BaseCEM
from psim.agents.entity import Disease, Population


class PSIMModel:
    def __init__(self, population: Population, disease: Disease):
        self.population = population
        self.disease = disease
        self.cems = defaultdict(list)
        # Randomly infect a person first
        u = choice(self.population.get_people())
        self.population.infect_person(u)
        print('Infected with virus:', u)

    def register_cem(self, target_week: int, cem: BaseCEM):
        self.cems[target_week].append(cem)

    def simulate_one_step(self):
        self.disease.infection_function(self.population)

    def simulate(self):
        pass


