from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = ""

        result += f"{self.name} Main Service:\n"

        if self.robots:
            names = ' '.join([r.name for r in self.robots])
            result += f"Robots: {names}"

        else:
            result += "Robots: none"

        return result