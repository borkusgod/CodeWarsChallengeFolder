def closest_multiple_10(i):
    print(i)
    if i == 0:
        return 10
    x = round(i)
    i = x
    i2str = str(i)
    last = i2str[-1]
    n = int(last)
    if 1 <= n <= 4:
        # print('will round down')
        empty_container = []
        for each in i2str:
            empty_container.append(each)
        empty_container.pop()
        empty_container.append(0)
        combine = ''
        for each in empty_container:
            each2str = str(each)
            combine = combine + each2str
        final_output = int(combine)
        return final_output
    if n > 4:
        # print('will round up')
        empty_container = []
        for each in i2str:
            empty_container.append(each)
        empty_container.pop()
        empty_container.append(0)
        combine = ''
        for each in empty_container:
            each2str = str(each)
            combine = combine + each2str
        final_output = int(combine) + 10
        return final_output
    if n == 0:
        # print('will round up')
        empty_container = []
        for each in i2str:
            empty_container.append(each)
        empty_container.pop()
        empty_container.append(0)
        combine = ''
        for each in empty_container:
            each2str = str(each)
            combine = combine + each2str
        final_output = int(combine) - 10
        return final_output


test_var1 = 54
test_var2 = 55
test_var3 = 105
test_var4 = 9470
test_var5 = 6420
test_var6 = 1676.0352305253590
test_var7 = 0
test_var8 = 10


print(closest_multiple_10(test_var1))
print('\n')
print(closest_multiple_10(test_var2))
print('\n')
print(closest_multiple_10(test_var3))
print('\n')
print(closest_multiple_10(test_var4))
print('\n')
print(closest_multiple_10(test_var5))
print('\n')
print(closest_multiple_10(test_var6))
print('\n')
print(closest_multiple_10(test_var7))
print('\n')
print(closest_multiple_10(test_var8))
print('\n')

