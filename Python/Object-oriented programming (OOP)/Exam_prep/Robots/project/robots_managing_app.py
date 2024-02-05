from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOTS_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPES[service_type](name)

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS_TYPES:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if (type(robot).__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService") or (type(robot).__name__ == "MaleRobot" and service.__class__.__name__ == "MainService"):

            if len(service.robots) >= service.capacity:
                raise Exception("Not enough capacity for this robot!")

            self.robots.remove(robot)
            service.robots.append(robot)

        else:
            return "Unsuitable service."

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]

        number_of_robots_fed = 0

        for robot in service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]

        total_price = sum([robot.price for robot in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

