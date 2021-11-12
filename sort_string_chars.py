def strsort(a_string):
    return ''.join(sorted(a_string))


# print(strsort('python'))


def even_odd_sum(sequence):
    my_list = []
    sum_odd = 0
    sum_even = 0
    for nr in sequence:
        if sequence.index(nr) % 2 == 0:
            sum_odd += nr
        else:
            sum_even += nr
    my_list.append(sum_odd)
    my_list.append(sum_even)
    return my_list


print(even_odd_sum([10, 20, 30, 40, 50, 60]))


def plus_minus(sequence):
    result = 0
    for nr in sequence:
        if sequence.index(nr) % 2 != 0:
            result += nr
        else:
            result -= nr
    return result


print(plus_minus([10, 20, 30, 40, 50, 60]))


def convert_to_int(my_num):
    return int(my_num)


def my_input_list():
    my_list = [my_in for my_in in input("Gime me some numbers: ").split(",")]
    my_int_list = []
    for nr in my_list:
        try:
            my_nr = int(nr)
            my_int_list.append(my_nr)
        except ValueError:
            print(f'Not valid for conversion {nr} to int')
    return my_int_list


def plus_minus():
    my_list = my_input_list()
    my_sum = my_list[0]
    for nr in my_list[1:]:
        if my_list.index(nr) % 2 != 0:
            my_sum += nr
        else:
            my_sum -= nr
    return my_sum


print(plus_minus())
