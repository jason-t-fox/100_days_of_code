def add_func(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(total)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


add_func(1, 2, 3, 4, 5, 6)
calculate(2, add=3, multiply=5)
