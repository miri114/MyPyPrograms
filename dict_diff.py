def dict_diff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),
                           second.get(key)]

    return output


d1 ={'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 5, 'b': 7, 'd': 3}
print(dict_diff(d1, d2))
