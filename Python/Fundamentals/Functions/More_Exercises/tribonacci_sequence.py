"""In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space,
starting from 1. You will receive a positive integer number as input."""

def tribonacci_conditions(n):
    if (n == 0 or n == 1 or n == 2):
        return 1
    elif (n == 3):
        return 2
    else:
        return (tribonacci_conditions(n - 1) +
                tribonacci_conditions(n - 2) +
                tribonacci_conditions(n - 3))


def tribonacci_invoke(n):
    for i in range(1, n+1):
        print(tribonacci_conditions(i), end=" ")


n = int(input())
tribonacci_invoke(n)