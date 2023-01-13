number = int(input())
reference_word = input()

full_list = []
reference_word_list = []

for current_word in range(number):
    current_word = input()
    full_list.append(current_word)

    if reference_word in current_word:
        reference_word_list.append(current_word)

print(full_list)
print(reference_word_list)