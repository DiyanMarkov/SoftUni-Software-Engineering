text = input()

vowels_list = ['a', 'o', 'u', 'e', 'i']

new_text = [char for char in text if char not in vowels_list]
print(''.join(new_text))
