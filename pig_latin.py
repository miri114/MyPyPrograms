def pig_latin():
    vowel = ['a', 'e', 'i', 'o', 'u', 'w', 'y']
    my_string = input("What is your secret language: \n")
    my_list = my_string.split()

    for word in my_list:
        if word[0] in vowel:
            print("".join([word, 'way']))
        else:
            print("".join([word[1:], word[0:1], 'ay']))


pig_latin()


def pig_latin_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)


print(pig_latin_sentence("This is a simple test to try if another is"))
