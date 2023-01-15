#import numpy as np

#example_list = np.array([10, 20, 30, 40, 50])

#print(example_list)



list2 = ['basic', 'fund', 'adv', 3]

list = [1, 5, 3, 2, 4]
list.copy()
print(list)
list.sort()
print(list.copy())
list.pop(3)
print(list)
list.reverse()
print(list)
list.append(4)
print(list)
list.sort()
print(list)
list.insert(4, 'monkeyboy')
print(list)
list.extend(list2)
print(list)
print(list.count(3))
list.remove(3)
print(list)
