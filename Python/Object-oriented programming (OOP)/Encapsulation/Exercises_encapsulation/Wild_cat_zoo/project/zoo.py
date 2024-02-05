from project import Animal
from Test_worker.project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > len(self.animals):

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)

            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_amount = sum([w.salary for w in self.workers])

        if self.__budget >= needed_amount:
            self.__budget -= needed_amount
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_amount = sum([a.money_for_care for a in self.animals])

        if self.__budget >= needed_amount:
            self.__budget -= needed_amount

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"

        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"

        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"

        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"

        keepers = [l for l in self.workers if l.__class__.__name__ == "Keeper"]
        caretakers = [t for t in self.workers if t.__class__.__name__ == "Caretaker"]
        vets = [c for c in self.workers if c.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"

        for k in keepers:
            result += f"{k}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for c in caretakers:
            result += f"{c}\n"

        result += f"----- {len(vets)} Vets:\n"

        for v in vets:
            result += f"{v}\n"

        return result[:-1]