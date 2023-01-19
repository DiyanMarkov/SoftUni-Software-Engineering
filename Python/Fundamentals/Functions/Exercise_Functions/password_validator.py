pass_is_valid = False

def pass_long_enough(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return
def is_pass_digits_letters(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return

def pass_at_least_two_digits(password):
    digit_counter = 0
    for digit in password:
        if digit.isdigit():
            digit_counter += 1
        if digit_counter >= 2:
            return True
    print("Password must have at least 2 digits")
    return


command_pass = input()

validated = [pass_long_enough(command_pass), is_pass_digits_letters(command_pass), pass_at_least_two_digits(command_pass)]

if all(validated):
    print("Password is valid")