class sequence_repeat:

    def __init__(self, sequence:str, number: int):
        self.sequence = sequence
        self.number = number + 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number - 1 == 0:
            raise StopIteration

        self.number -= 1
        self.index += 1

        if self.index == len(self.sequence):
            self.index = 0

        return self.sequence[self.index]




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
