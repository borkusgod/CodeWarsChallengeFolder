import re


def reverse_words(text):
    print(text)

    formatted_string = ''
    string_split = text.split(" ")
    for each in string_split:
        print(each)
        print(type(each))
        print(len(each))
        if len(each) > 0:
            word_container = ''
            for each_let in each:
                word_container += each_let
            # print(word_container)
            word_revved = word_container[::-1]
            print(word_revved)
            formatted_string = formatted_string + word_revved + ' '
    final_out = ''.join(formatted_string)
    print(type(final_out))
    print(len(final_out))
    return final_out


test_string1 = 'The quick brown fox jumps over the lazy dog.'
test_string2 = 'apple'
test_string3 = 'a b c d'
test_string4 = 'double  spaced  words'

print(reverse_words(test_string1))
print('\n')
print(reverse_words(test_string2))
print('\n')
print(reverse_words(test_string3))
print('\n')
print(reverse_words(test_string4))
print('\n')