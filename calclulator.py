def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


def mod(a, b):
    return a % b


def calc(to_solve):
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
        '**': pow,
        '%': mod
    }
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)


print(calc('** 2 3'))
