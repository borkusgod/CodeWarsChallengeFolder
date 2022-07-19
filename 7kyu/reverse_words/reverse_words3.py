# solution taken from dicussions. tired of monkeying around with and
# time to move on to something else

def reverse_words(str):
    newstr = []
    for i in str.split(' '):
        newstr.append(i[::-1])
    return ' '.join(newstr)


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