from collections import deque

tools = deque(int(x) for x in input().split())  #popleft()
substances = deque(int(x) for x in input().split()) #pop()
challenges = deque(int(x) for x in input().split()) # iterate for =

challenges_copy = challenges.copy()

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance

    if result not in challenges:
        tool += 1
        tools.append(tool)

        substance -= 1

        if substance > 0:
            substances.append(substance)

        else:
            continue


    else:
        for c in challenges_copy:
            if result == c:
                challenges.remove(c)
                break

if not (tools and substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")