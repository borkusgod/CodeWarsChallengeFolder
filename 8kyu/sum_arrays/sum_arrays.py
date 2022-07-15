def sum_array(a):
    if a == 0:
        return 0
    empty_var = 0
    for each in a:
        empty_var = empty_var + each
    return empty_var


print(sum_array([1, 5.2, 4, 0, -1]))

