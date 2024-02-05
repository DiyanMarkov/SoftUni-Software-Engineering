times = int(input())

unique = set()

for i in range(times):
    name = input()
    unique.add(name)

print('\n'.join((unique)))



#times = int(input())

#unique = []

#for i in range(times):
    #name = input()
    #unique.append(name)

#print('\n'.join(set(unique)))