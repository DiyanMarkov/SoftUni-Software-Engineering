class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)


    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"

        return result


zoo_name = input()
n = int(input())
object_zoo = Zoo(zoo_name)

for animal in range(n):
    current_animal = input().split(' ')
    species, name = current_animal
    object_zoo.add_animal(species, name)

info_about_species = input()
print(object_zoo.get_info(info_about_species))