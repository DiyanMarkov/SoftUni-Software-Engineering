from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish,
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = next((d for d in self.divers if d.name == diver_name), None)

        if diver:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)

        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)

        if fish:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)

        self.fish_list.append(new_fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)


        if not diver:
            return f"{diver_name} is not registered for the competition."


        fish = next((f for f in self.fish_list if f.name == fish_name),None)


        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)

            if diver.oxygen_level <= 0:
                diver.has_health_issue = True

            if diver.has_health_issue:
                return f"{diver_name} will not be allowed to dive, due to health issues."

            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)

                if diver.oxygen_level == 0:
                    diver.has_health_issue = True

                if diver.has_health_issue:
                    return f"{diver_name} will not be allowed to dive, due to health issues."

                diver.catch.append(fish)

                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            if not is_lucky:
                diver.miss(fish.time_to_catch)

                if diver.oxygen_level == 0:
                    diver.has_health_issue = True

                if diver.has_health_issue:
                    return f"{diver_name} will not be allowed to dive, due to health issues."

                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)

            if diver.oxygen_level == 0:
                diver.has_health_issue = True

            if diver.has_health_issue:
                return f"{diver_name} will not be allowed to dive, due to health issues."

            diver.catch.append(fish)

            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers = [d for d in self.divers if d.has_health_issue]

        counter_divers_recovered = 0

        for diver in divers:
            diver.has_health_issue = False
            diver.oxygen_level = diver.renew_oxy()
            counter_divers_recovered += 1

        return f"Divers recovered: {counter_divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)

        result = [f"**{diver_name} Catch Report**"]
        fishes_info = '\n'.join(f.fish_details() for f in diver.catch)

        result.append(fishes_info)

        return '\n'.join(result)

    def competition_statistics(self):

        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        final_divers = [d for d in sorted_divers if not d.has_health_issue]

        result = ["**Nautical Catch Challenge Statistics**"]

        diver_info = '\n'.join(str(u) for u in final_divers)
        result.append(diver_info)

        return "\n".join(result)






