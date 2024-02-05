from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0


while milkshakes != 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue

    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
        continue

    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        chocolates.append(current_chocolate - 5)
        cups_of_milk.append(current_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")