import math


def is_square(n):
    number = int(n)
    if number < 0:
        return False
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        # print(number, "is a perfect square")
        return True
    else:
        # print(number, "is not a perfect square")
        return False


test_int1 = -1
test_int2 = 0
test_int3 = 3
test_int4 = 4
test_int5 = 25
test_int6 = 26

print(is_square(test_int1))
print('\n')
print(is_square(test_int2))
print('\n')
print(is_square(test_int3))
print('\n')
print(is_square(test_int4))
print('\n')
print(is_square(test_int5))
print('\n')
print(is_square(test_int6))
print('\n')

