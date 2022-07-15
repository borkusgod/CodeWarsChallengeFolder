import math


def odd_count(n):
    if n < 0:
        n = abs(n)
    for_counting = n + 1
    container_list = []
    if n == 1:
        container_list.append(n)
    for each in range(for_counting):
        if (each % 2) == 1:
            container_list.append(each)
    how_many = len(container_list)
    print(container_list)
    print(f'There are {how_many} odd numbers contained within the number you '
          f'input.')
    return f'Using odd_count to return how_many: {how_many}'


def odd_count2(n):
    if n == 0:
        print('return 0')
        return 0
    if n == 1:
        print('return 1')
        return 1
    half_n = n / 2
    return int(half_n)


print('func using 0')
print(odd_count(0))
print('o0-------')
print(odd_count2(0))
print('\n')
print('func using 1')
print(odd_count(1))
print('o0-------')
print(odd_count2(1))
print('\n')
print('func using 15')
print(odd_count(15))
print('o0-------')
print(odd_count2(15))
print('\n')
print('func using 25')
print(odd_count(25))
print('o0-------')
print(odd_count2(25))
print('\n')
# # odd_count(15023)
# print('\n')
# odd_count(-11)
# odd_count2(-11)

# print(odd_count(8414749120))

