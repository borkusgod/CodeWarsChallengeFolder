"""
Given a list of integers, determine whether the sum of its elements is
odd or even. Give your answer as a string matching "odd" or "even".
If the input array is empty, consider it as [0] (array with zero)
Be careful that is the integer is negative, it doesn't count
"""


def odd_or_even(arr):
    each_to_list = []
    list_with_zero = [0]
    sum_of = 0
    for_adding = 0
    if arr == each_to_list:
        return "even"
    for each in arr:
        to_int = int(each)
        if to_int >= 0:
            print(f'added to each_to_list: {to_int}')
            each_to_list.append(to_int)
    add_together = sum(each_to_list)
    print(f'len of each_to_list: {len(each_to_list)}')
    len_of_list = len(each_to_list)
    print(add_together)
    if (add_together % 2) == 0:
        return 'even'
    else:
        return 'odd'


test1 = [0]
test2 = [0, 1, 3]
test3 = [0, 1, 2]
test4 = [1, 2, 3, 4]
test5 = [1, 2, 3, 4, 5]
test6 = []
test7 = [0, 1, -1, -2]
test8 = [-52, 97, -16, 81, 39, -62, -50, 98, -70, -1, 0]
test9 = [-3]
test10 = [1023, 1, 2]

print('test 1')
print(f'from array{test1}')
print(odd_or_even(test1))
print('\n')

print('test 2')
print(f'{test2}')
print(odd_or_even(test2))
print('\n')

print('test 3')
print(f'{test3}')
print(odd_or_even(test3))
print('\n')

print('test 4')
print(f'{test4}')
print(odd_or_even(test4))
print('\n')

print('test 5')
print(f'{test5}')
print(odd_or_even(test5))
print('\n')

print('test 6')
print(f'{test6}')
print(odd_or_even(test6))
print('\n')

print('test 7')
print(f'{test7}')
print(odd_or_even(test7))
print('\n')

print('test 8')
print(f'{test8}')
print(odd_or_even(test8))
print('\n')

print('test 9')
print(f'{test9}')
print(odd_or_even(test9))
print('\n')

print('test 10')
print(f'{test10}')
print(odd_or_even(test10))
