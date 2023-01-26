class Party:
    def __init__(self):
        self.people = []

    def invite_people(self, name):
        return self.people.append(name)

    def names_attendees(self):
        return ', '.join([name for name in self.people])

    def total_people(self):
        return len(self.people)

object = Party()

while True:
    command = input()

    if command == 'End':
        break

    name = command
    object.invite_people(name)

print(f"Going: {object.names_attendees()}")
print(f"Total: {object.total_people()}")