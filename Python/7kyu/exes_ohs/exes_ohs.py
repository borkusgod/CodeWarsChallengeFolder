def xo(s):
    print(s)
    x_container = ''
    o_container = ''
    for each in s:
        # print(each)
        each2lower = each.lower()
        print(each2lower)
        if each2lower == 'x':
            x_container += each2lower
        if each2lower == 'o':
            o_container += each2lower
    print(len(x_container))
    print(len(o_container))
    if len(x_container) == len(o_container):
        print('there are equal x\'s and o\'s')
        return True
    if len(x_container) != len(o_container):
        print('There are not equal x\'s and o\'s')
        return False


string1 = 'ooxx'
string2 = 'xooxx'
string3 = 'ooxXm'
string4 = 'zpzpzpp'
string5 = 'zzoo'
string6 = 'xxmxOhxOpONJxOxrOCOEOOOLOOkOxxxQxOOOAGOxxxSObxxxfxd'
string7 = 'XO'

print(xo(string1))
print('\n')
print(xo(string2))
print('\n')
print(xo(string3))
print('\n')
print(xo(string4))
print('\n')
print(xo(string5))
print('\n')
print(xo(string6))
print('\n')
print(xo(string7))
print('\n')
