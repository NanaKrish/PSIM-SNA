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
        self.current_iteration = 0
        self.population.infect_person(u)
        print('Infected with virus:', u)

    def register_cem(self, target_iteration: int, cem: BaseCEM):
        self.cems[target_iteration].append(cem)

    def simulate_one_step(self):
        self.current_iteration += 1
        print(f'\n>>> Current Iteration: {self.current_iteration}')

        if self.cems.get(self.current_iteration - 1) is not None:
            for cem in self.cems.get(self.current_iteration - 1):
                cem.relax_enforcement()

        if self.cems.get(self.current_iteration) is not None:
            for cem in self.cems.get(self.current_iteration):
                cem.enforce()

        self.disease.infection_function(self.population)

    def simulate(self):
        pass
