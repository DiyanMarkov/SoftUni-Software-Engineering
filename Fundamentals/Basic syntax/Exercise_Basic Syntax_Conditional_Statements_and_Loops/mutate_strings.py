string1 = input()
string2 = input()
last_word = ''

for i in range(len(string1)):
    up_word = string2[:i + 1]
    down_word = string1[i + 1:]

    new_word = up_word + down_word

    if last_word == new_word:
        continue

    last_word = new_word
    print(new_word)