from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - (time_to_catch * 0.30) < 0:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= time_to_catch * 0.30

            if isinstance(self.oxygen_level, float):
                round(self.oxygen_level)

    def renew_oxy(self):
        return self.oxygen_level == 540

