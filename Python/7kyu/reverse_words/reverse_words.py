import re


def reverse_words(text):
    print(text)
    print(type(text))
    if '.' in text:
        print('true')
    formatted_container = []
    final_out = ''
    regex_splitter = re.split(' ', text)
    # print(regex_splitter)
    for each in regex_splitter:
        temp_word = ''
        if len(each) < 2:
            formatted_container.append(each)
        if len(each) >= 2:
            for each_let in each:
                temp_word += each_let
        temp_revved = temp_word[::-1]
        # print(temp_word)
        # print(temp_revved)
        formatted_container.append(temp_revved)
    for each in formatted_container:
        final_out += each + ' '
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