def print_row(n, el):
    print(" " * (n - el), end="")
    print(*['*'] * el)


def top_half(n):
    for el in range(1, n + 1):
        print_row(n, el)


def bottom_half(n):
    for el in range(n - 1, 0, -1):
        print_row(n, el)


def rhombus(n):
    top_half(n)
    bottom_half(n)


n = int(input())

rhombus(n)
