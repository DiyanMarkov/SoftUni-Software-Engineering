from collections import deque

q = deque(input().split())
toss = int(input())

counter = 0

while len(q) > 1:

    counter += 1

    if counter == toss:
        removed_kid = q.popleft()
        print(f"Removed {removed_kid}")
        counter = 0

    else:
        removed_kid = q.popleft()
        q.append(removed_kid)

print(f"Last is {q[0]}")


#from collections import deque

#q = deque(input().split())

#toss = int(input())

#while len(q) != 1:
    #q.rotate(-(toss-1))
    #print(f'Removed {q.popleft()}')

#print(f"Last is {q.popleft()}")
