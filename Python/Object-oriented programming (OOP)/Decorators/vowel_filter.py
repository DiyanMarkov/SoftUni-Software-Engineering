def vowel_filter(function):
    def wrapper():
        VOWELS = ["a", "e", "o", "u", "i"]
        result = function()

        return [x for x in result if x in VOWELS]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
