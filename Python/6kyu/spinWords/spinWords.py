# make a function that will take any word that is longer then five characters
# and reverses them.
# stringExample = 'stop spinning my words around'
# reversed: stop gninnips my sdrow dnuora

def spin_words(sentence):
    fromfunc2list = []
    back2string = ""
    using_split = sentence.split(' ')
    for each in using_split:
        if len(each) >= 5:
            each_rev = each[::-1]
            fromfunc2list.append(each_rev)
        else:
            fromfunc2list.append(each)
    for each in fromfunc2list:
        back2string += each
        back2string += ' '
    print(back2string)
    strip_out = back2string.strip()
    return strip_out


test_1 = 'stop spinning my words around'
test_2 = 'this is another test with small word ex'
test_3 = 'no word with five or more'
test_4 = 'to'
test_5 = 'welcome'
test_6 = 'Hey fellow warriors'
test_7 = 'This is a test'

print(test_1)
spin_words(test_1)
print('\n')
print(test_2)
spin_words(test_2)
print('\n')
print(test_3)
spin_words(test_3)
print('\n')
print(test_4)
spin_words(test_4)
print('\n')
print(test_5)
spin_words(test_5)
print('\n')
print(test_6)
spin_words(test_6)
print('\n')
print(test_7)
spin_words(test_7)