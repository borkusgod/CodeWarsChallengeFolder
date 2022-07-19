def get_count(sentence):
    vowel_dict = ('a', 'e', 'i', 'o', 'u')
    if sentence is None or sentence == '':
        return 0
    vowel_count = 0
    for each in sentence:
        if each in vowel_dict:
            vowel_count += 1
    print(f'There are {vowel_count} vowels in the test string.')
    return vowel_count


string1 = "aeiou"
string2 = "y"
string3 = "bcdfghjklmnpqrstvwxz y"
string4 = ""
string5 = "abracadabra\""

print(get_count(string1))
print('\n')
print(get_count(string2))
print('\n')
print(get_count(string3))
print('\n')
print(get_count(string4))
print('\n')
print(get_count(string5))
print('\n')


