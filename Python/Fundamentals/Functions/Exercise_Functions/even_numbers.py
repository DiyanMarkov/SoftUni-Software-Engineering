numbers_as_digits = [int(num) for num in input().split(' ')]
result = list(filter(lambda num: num % 2 == 0, numbers_as_digits))
print(result)