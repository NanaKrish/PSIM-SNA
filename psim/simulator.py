from collections import defaultdict
from copy import deepcopy
from typing import Dict, List

from psim.agents.cem import BaseCEM, SocialDistancing
from psim.agents.entity import Disease, Population, Location
from psim.utils.helpers import load_user_data


class PSIMModel:
    def __init__(self, population: Population, disease: Disease):
        self.population = population
        self.disease = disease
        self.cems: Dict[int, List[BaseCEM]] = defaultdict(list)
        self.current_week = 0

    def register_cem(self, target_week: int, cem: BaseCEM):
        self.cems[target_week].append(cem)

    def __activate_cem(self):
        if self.cems.get(self.current_week) is None:
            return 0
        for cem in self.cems[self.current_week]:
            pass

    def simulate(self):
        while self.population.get_population_status()["healthy"]:
            pass


if __name__ == '__main__':
    data = load_user_data("D:\Programming\Python\PSIM\psim\input.csv")
    p = Population(data)
    mat = Location.calculate_distance_matrix(p)
    t = deepcopy(mat)
    print("Mat", mat)
    smat = SocialDistancing.activate_enforcement(mat, safe_distance=1000)
    print(mat)
    print(t==smat)
    SocialDistancing.relax_enforcement(mat)
    print("Mat", mat)
