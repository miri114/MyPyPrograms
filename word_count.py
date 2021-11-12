import time

def word_count(filename):
    counts = {
        'characters': 0,
        'words': 0,
        'lines': 0
    }

    unique_words = set()
    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())

        unique_words.update(one_line.split())

    counts['unique_words'] = len(unique_words)

    for key, value in counts.items():
        print(f'{key}: {value}')


word_count('test_text.txt')




user_input = input("Pls first give the file name and than words to "
                   "calculate frequencies: \n").split(',')
my_file = user_input[0] + '.txt'
words_to_count = user_input[1:]
# print(my_file)
# print(" \n Word to count: ", words_to_count)


start = time.time()


def words_frequency():
    word_dict = {el: 0 for el in words_to_count}
    print(word_dict)
    for one_line in open(my_file):
        for word in one_line.split():
            if word in word_dict.keys():
                word_dict[word] += 1
    print(word_dict)


words_frequency()

# def test_frequency():
#     my_dict = {}
#     for elemn in words_to_count:
#         counter = 0
#         for one_line in open(my_file):
#             for word in one_line.split():
#                 if word == elemn:
#                     print(word)
#                     counter += 1
#                     my_dict[elemn] = counter
#     print(my_dict)
#
# test_frequency()

print(time.time() - start)
# print(start2 - start1)


