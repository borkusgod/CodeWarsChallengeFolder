def find_short(s):
    # your code here
    each_word = s.split(' ')
    container = []
    for each in each_word:
        len_of = len(each)
        # print(len_of)
        container.append(len_of)
    small_of = min(container)
    return small_of


string1 = 'bitcoin take over the world maybe who knows perhaps'
string2 = 'turns out random test cases are easier than writing out basic ones'
string3 = 'lets talk about javascript the best language'
string4 = 'i want to travel the world writing code one day'
string5 = 'Lets all go on holiday somewhere very cold'
string6 = 'Let\'s travel abroad shall we'

print(find_short(string1))
print('\n')
print(find_short(string2))
print('\n')
print(find_short(string3))
print('\n')
print(find_short(string4))
print('\n')
print(find_short(string5))
print('\n')
print(find_short(string6))
print('\n')
