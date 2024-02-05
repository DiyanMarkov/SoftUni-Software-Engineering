class dictionary_iter:

    def __init__(self, dict_obj):
        self.dict_obj = list(dict_obj.items())
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations >= len(self.dict_obj) - 1:
            raise StopIteration

        self.iterations += 1

        return self.dict_obj[self.iterations]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


