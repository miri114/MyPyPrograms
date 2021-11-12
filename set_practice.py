from collections import Counter


def how_many_numbers(numbers):
    unique_numbers = set(numbers)
    return unique_numbers


print(how_many_numbers([1, 2, 3, 1, 2, 3, 4, 1]))


def some_numbers_to_dict():
    numbers = [1, 2, 3, 1, 2, 3, 4, 1]
    my_counter = Counter(numbers)
    return dict(my_counter)


print(some_numbers_to_dict())