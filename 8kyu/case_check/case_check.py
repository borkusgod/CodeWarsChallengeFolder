"""
write a function that will check if two given characters are the same case
if either of characters is not a letter, return -1
if both characters are the same case, return 1
if both characters are letters, but not the same case, return 0
a - a = 1
A - A = 1
a - A = 0
a - ? = -1
"""


def same_case(a, b):
    if a.islower() and b.islower():
        print(f'{a} {b}')
        # print('1')
        return 1
    if a.isupper() and b.isupper():
        print(f'{a} {b}')
        # print('1')
        return 1
    if a.islower() and b.isupper():
        print(f'{a} {b}')
        # print('0')
        return 0
    if a.isupper() and b.islower():
        print(f'{a} {b}')
        # print('0')
        return 0
    if not a.isalpha() or not b.isalpha():
        print(f'{a} {b}')
        # print('-1')
        return -1


lower_let = 'a'
upper_let = 'A'
non_let = '?'
print(same_case(lower_let, upper_let))

