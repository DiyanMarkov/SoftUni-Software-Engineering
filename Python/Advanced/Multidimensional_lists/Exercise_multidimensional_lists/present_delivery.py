def eat_cookie(presents_left, nice_kids):  # създаваме фунцкия, първи параметър останалите подаръци и втори добрите деца
    for coordinates in directions.values():  # обхождаме всяка посока от посоките
        r = santa_pos[0] + coordinates[0]  # намираме реда като съберем реда на Дядо Коледа и реда от посоката
        c = santa_pos[1] + coordinates[1]  # намираме колоната като съберем колоната на Дядо Коледа и тази от посоката

        if matrix[r][c].isalpha():  # проверяваме дали сме стъпили на буква
            if matrix[r][c] == 'V':  # проверяваме дали сме в къщата на добро дете
                nice_kids += 1  # увеличаваме броя на посетените добри деца за скоупа на функцията

            matrix[r][c] = '-'  # заменяме позицията, на която сме с тире
            presents_left -= 1  # намаляме наличните подаръци с 1, в скоупа на функцията

        if not presents_left:  # проверяваме дали са ни свършили подаръците
            break  # прекратяваме цикъла

    return presents_left, nice_kids  # връщаме наличните подаръци и броя на посетените добри деца


presents = int(input())

rows = int(input())
cols = rows

total_nice_kids = 0
nice_kids_received = 0


matrix = []

santa_pos = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):

        if matrix[row][col] == 'S':
            santa_pos = [row, col]
            matrix[row][col] = "-"

        elif matrix[row][col] == 'V':
            total_nice_kids += 1


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()

while command != 'Christmas morning':

    santa_pos = [santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]]  # get the coordinates (r,c)

    if not (0 <= santa_pos[0] < rows and 0 <= santa_pos[1] < cols):
        command = input()
        continue

    if matrix[santa_pos[0]][santa_pos[1]] == "-":
        command = input()
        continue

    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        presents -= 1
        nice_kids_received += 1

    if house == 'C':
        presents, nice_kids_received = eat_cookie(presents, nice_kids_received)

    matrix[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_received == total_nice_kids:
        break

    command = input()


matrix[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and total_nice_kids-nice_kids_received > 0:
    print(f"Santa ran out of presents!")

[print(*el) for el in matrix]

if total_nice_kids == nice_kids_received:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')

else:
    print(f'No presents for {total_nice_kids-nice_kids_received} nice kid/s.')