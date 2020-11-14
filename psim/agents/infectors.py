from psim.agents.entity import Disease


class COVID19(Disease):
    def __init__(self, infectivity: float, infection_radius: float, infection_type: str):
        super().__init__(infectivity, infection_radius, infection_type)

    def infection_function(self):
        # TODO: Implement infection function
        pass
