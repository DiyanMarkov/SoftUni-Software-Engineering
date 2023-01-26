class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

name = Person('Mario', 'Ivanov', 22)
print(name.first_name, name.last_name, name.age)