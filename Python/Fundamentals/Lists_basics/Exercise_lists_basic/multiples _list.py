factor = int(input())
list_lenght = int(input())

generated_list = []

for i in range(1, list_lenght + 1):
    new_number = factor * int(i)
    generated_list.append(new_number)

print(generated_list)


