searched_book = input()

checked_books = 0
current_book = input()

while current_book != searched_book:

    if current_book != searched_book:
        if current_book == 'No More Books':
            break

    if current_book == searched_book:
        break

    checked_books += 1
    current_book = input()


if current_book == searched_book:
    print(f'You checked {checked_books} books and found it.')

if current_book != searched_book:
    print(f'The book you search is not here!')
    print(f'"You checked {checked_books} books."')