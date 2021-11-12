import random
from itertools import count


def create_password_generator(characters):
    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password


#alpha_password = create_password_generator('abcdef')
#symbol_password = create_password_generator('!£$%^&*@')


#print(create_password_generator('abcdef')(10))


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def give_pass_string():
        my_upp = 0
        my_low = 0
        my_punc = 0
        my_digit = 0
        my_pass = input("Write the password: \n")
        my_pass_list = list(my_pass)
        for letter in my_pass_list:
            if letter.isupper():
                my_upp += 1
            elif letter.islower():
                my_low += 1
            elif letter.isdigit():
                my_digit += 1
            else:
                my_punc += 1
        if my_upp >= min_uppercase and my_low >= min_lowercase and my_digit >= min_digits and my_punc >= min_punctuation:
            return True
        else:
            return False
    return give_pass_string


my_passwordi = create_password_checker(1,1,1,1)

print(my_passwordi())





