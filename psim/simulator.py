from collections import defaultdict

from psim.agents.cem import BaseCEM
from psim.agents.entity import Disease, Population


class PSIMModel:
    def __init__(self, population: Population, disease: Disease):
        self.population = population
        self.disease = disease
        self.cems = defaultdict(list)

    def register_cem(self, target_week: int, cem: BaseCEM):
        self.cems[target_week].append(cem)

    def simulate(self):
        pass
