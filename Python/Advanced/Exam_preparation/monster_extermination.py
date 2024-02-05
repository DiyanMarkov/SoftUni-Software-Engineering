from collections import deque

armors = deque(int(x) for x in input().split(","))  #popleft()
monsters_armor = armors.copy()
strikings = deque(int(x) for x in input().split(",")) #pop()

while armors and strikings:
    armor = armors.popleft()
    strike = strikings.pop()

    if strike == armor:
        continue

    elif strike > armor:
        strike -= armor
        if strikings:
            strikings[-1] += strike
        else:
            strikings.append(strike)

    elif armor > strike:
        armor -= strike
        armors.append(armor)

if not armors:
    print(f"All monsters have been killed!")

if not strikings:
    print(f"The soldier has been defeated.")

print(f"Total monsters killed: {len(monsters_armor) - len(armors)}")