repeated_string = input()
repeat_counter = int(input())

new_string = lambda old_string, repeat_counter: old_string*repeat_counter
print(new_string(repeated_string, repeat_counter))

