from collections import deque

vowels = deque(input().split()) # popleft()
consonants = deque(input().split()) # pop()

searched_words = {"rose": "rose", "lotus": "lotus", "tulip": "tulip", "daffodil": "daffodil"}
searched_copy = searched_words.copy()

found_word = False

while vowels and consonants and found_word == False:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in searched_copy:
        searched_copy[word] = searched_copy[word].replace(current_vowel, "")
        searched_copy[word] = searched_copy[word].replace(current_consonant, "")

        if searched_copy[word] == "":
            print(f"Word found: {word}")
            found_word = True
            break

if found_word == False:
    print("Cannot find any word!")

if vowels:
    result = ' '.join(vowels)
    print(f"Vowels left: {result}")

if consonants:
    result = ' '.join(consonants)
    print(f"Consonants left: {result}")