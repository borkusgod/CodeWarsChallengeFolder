def get_middle(s):
    print(s)
    # get len first
    if len(s) == 1 or len(s) == 2:
        return s
    len_of_s = len(s)
    if (len_of_s % 2) == 0:
        print('input string has even characters')
        get_half = len_of_s / 2
        # print(get_half)
        left_ind = (int(get_half)) - 1
        right_ind = int(get_half)
        mid_l = s[left_ind]
        mid_r = s[right_ind]
        return f'{mid_l}{mid_r}'

    if (len_of_s % 2) == 1:
        print('input string has odd characters')
        get_half = len_of_s / 2
        # print(get_half)
        gh_2_int = int(get_half)
        # print(gh_2_int)
        # print(s[gh_2_int])
        return s[gh_2_int]


string1 = 'test'
string2 = 'testing'
string3 = 'middle'
string4 = 'A'
string5 = 'of'

print(get_middle(string1))
print('\n')
print(get_middle(string2))
print('\n')
print(get_middle(string3))
print('\n')
print(get_middle(string4))
print('\n')
print(get_middle(string5))
print('\n')
