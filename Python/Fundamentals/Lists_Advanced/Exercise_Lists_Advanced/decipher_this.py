message = input().split()
final_message = []
for word in message:
    digits = ''

    for index in word:
        if index.isdigit():
            digits += index

    word = word.replace(digits, '')
    if len(word) >= 2:
        word = word[-1] + word[1:-1] + word[0]
    digits = int(digits)
    digits = chr(digits)
    current_message = f'{digits}{word}'
    final_message.append(current_message)

print(' '.join(final_message))