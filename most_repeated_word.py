from collections import Counter
import operator


def user_input_to_list():
    my_input = input("Give me some strings: \n")
    my_list = my_input.split()
    return my_list


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word():
    my_words = user_input_to_list()
    return max(my_words,
               key=most_repeating_letter_count(1)[0][1])


print(most_repeating_word())


""" UNFINISHED """