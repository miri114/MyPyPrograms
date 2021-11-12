def mysum(*numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum


print(mysum(10, 20, 30, 40, 50))


def my_sum(*args):
    if not args:
        return args
    output = args[0]
    for args in args[1:]:
        output += args
    return output


print(my_sum([10,20,30]))
