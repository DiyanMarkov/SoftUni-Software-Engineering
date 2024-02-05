from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self .VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if team1.__class__.__name__ != team2.__class__.__name__: #type(team1) != type(team2)
            raise Exception("Game cannot start! Team types mismatch!")

        team1_advantage_points = team1.advantage + sum(e.protection for e in team1.equipment)
        team2_advantage_points = team2.advantage + sum(e.protection for e in team2.equipment)

        if team1_advantage_points > team2_advantage_points:
            team1.win()
            return f"The winner is {team1.name}."

        if team1_advantage_points < team2_advantage_points:
            team2.win()
            return f"The winner is {team2.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)

        result = [f"Tournament: {self.name}",
                 f"Number of Teams: {len(sorted_teams)}",
                 f"Teams:"]

        [result.append(t.get_statistics()) for t in sorted_teams]

        return "\n".join(result)