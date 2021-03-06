from psim.agents.entity import Disease, Population


class COVID19(Disease):
    THRESHOLD_TIME = 7

    def __init__(self, infectivity: float, infection_radius: float, infection_type: str):
        super().__init__(infectivity, infection_radius, infection_type)
        self.elapsed_time = 0

    def calculate_time(self, weight):
        if weight < 0.3:
            return 10
        elif weight < 0.45:
            return 7
        elif weight < 0.6:
            return 5
        elif weight < 0.75:
            return 4
        else:
            return 3

    def infection_function(self, population: Population):
        g = population.get_graph()
        timef = []
        for infected_person in population.get_population_status(raw=True)['infected']:
            adjacent_edges = g.edges(infected_person, data=True)
            for u, v, d in adjacent_edges:
                weight = d['weight']
                time = 0
                if v.healthy:
                    time = self.calculate_time(weight)
                    if time < self.THRESHOLD_TIME:
                        population.infect_person(v)
                g.edges[u, v]['time'] = time

            for u, v, d in adjacent_edges:
                if not v.healthy:
                    timef.append(d['time'])
        f = max(timef)
        self.elapsed_time += f
