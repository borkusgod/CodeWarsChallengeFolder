def sum_array(arr):
    # print(f'from input: {arr}')
    if arr is None:
        return 0
    if arr == []:
        return 0
    if len(arr) == 1 or len(arr) == 2:
        return 0
    if len(arr) > 2:
        empty_container = 0
        # print(arr)
        arr.sort()
        # print(arr)
        arr.pop(0)
        # print(arr)
        arr.pop()
        for each in arr:
            empty_container = empty_container + each
        # print(arr)
        # return f'return list with largest and smallest removed: ' \
        #        f' {empty_container}'
        return empty_container

# real arrayz
arr1 = [6, 2, 1, 8, 10]
arr2 = [6, 0, 1, 10, 10]
arr3 = [-6, -20, -1, -10, -12]
arr4 = [-6, 20, -1, 10, -12]

# none type arrs for testing
none_arr = None
empty_arr = []

# one val arrs
one_arr = [3]
one_arr2 = [-3]

# two val arrs
two_arr = [ 3, 5]
two_arr2 = [-3, -5]

print('Test with multi-val arrs')
print(sum_array(arr1))
print(sum_array(arr2))
print(sum_array(arr3))
print(sum_array(arr4))
print('======\n')

print('Test with none type arrs')
print(sum_array(none_arr))
print(sum_array(empty_arr))
print('\n')

print('Test with one val arrs')
print(sum_array(one_arr))
print(sum_array(one_arr2))
print('\n')

print('Test with two val arrs')
print(sum_array(two_arr))
print(sum_array(two_arr2))
print('\n')