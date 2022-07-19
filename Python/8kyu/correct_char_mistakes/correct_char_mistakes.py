def correct(s):
    # print(s)
    list_container = []
    for each in s:
        if each == '5':
            each = 'S'
        if each == '0':
            each = 'O'
        if each == '1':
            each = 'I'
        # print(each)
        list_container.append(each)
    # print(list_container)
    list2string = ''.join(list_container)
    return list2string


char_set1 = 'L0ND0N'
char_set2 = 'DUBL1N'
char_set3 = '51NGAP0RE'
char_set4 = 'BUDAPE5T'
char_set5 = 'PAR15'

print(correct(char_set1))
print(correct(char_set2))
print(correct(char_set3))
print(correct(char_set4))
print(correct(char_set5))
