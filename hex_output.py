def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: \n')

    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 * power)
    print(decnum)


# hex_output()


def print_name_triangle():
    my_name = input("Enter your name: ")

    for index, value in enumerate(my_name):
        print(my_name[0:index + 1])


print_name_triangle()
