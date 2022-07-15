"""
You are given an array (which will have a length of at least 3,
but could be very large) containing integers. The array is either
entirely comprised of odd integers or entirely comprised of even
integers except for a single integer N. Write a method that takes
the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    if_even = []
    if_odd = []
    for each in integers:
        if (each % 2) == 0:
            if_even.append(each)
        if (each % 2) != 0:
            if_odd.append(each)
    if len(if_even) == 1:
        to_int = int(if_even[0])
        return to_int
    else:
        to_int = int(if_odd[0])
        return to_int


test1 = [2, 4, 0, 100, 4, 11, 2602, 36]
test2 = [160, 3, 1719, 19, 11, 13, -21]

print(find_outlier(test1))
print(find_outlier(test2))

