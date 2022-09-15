def ascend_descend(length, minimum, maximum):
    a = list(range(minimum, maximum + 1))
    b = list(range(maximum - 1, minimum - 1, -1))
    a_and_b = a + b
    if len(a_and_b) == 1:
        return ''.join(map(str,a_and_b * length))
    str_a_and_b = ''.join(map(str, a_and_b[:-1])) * length
    return str_a_and_b[:length]e


print(ascend_descend(5, 1, 3))
print('\n')
print(ascend_descend(14, 0, 2))
print('\n')
print(ascend_descend(11, 5, 9))
print('\n')