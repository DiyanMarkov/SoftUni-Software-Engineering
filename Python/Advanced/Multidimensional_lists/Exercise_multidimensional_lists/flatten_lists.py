data = [[el for el in sub_list.split()] for sub_list in input().split("|")][::-1]

sub_list = []

for sub_string in data:
    sub_list.extend(sub_string)

print(*sub_list, end=" ")