from typing import List


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return self.name + " " + other.surname


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people: List[Person] = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(x) for x in self.people])}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"
