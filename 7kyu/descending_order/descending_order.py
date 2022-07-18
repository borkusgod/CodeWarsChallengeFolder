def descending_order(num):
    if num == 0:
        return num
    print(num)
    num_2_str = str(num)
    print(f'num_2_str as str: {num_2_str}')
    list_container = []
    for each in num_2_str:
        # print(each)
        list_container.append(each)
    list_container.sort()
    list_container.sort(reverse=True)
    print(list_container)
    str_container = ''
    for each in list_container:
        str_container += each
    print(str_container)
    back2int = int(str_container)
    return back2int

int1 = 0
int2 = 15
int3 = 123456789
int4 = 42145
int5 = 145263

print(descending_order(int1))
print('\n')
print(descending_order(int2))
print('\n')
print(descending_order(int3))
print('\n')
print(descending_order(int4))
print('\n')
print(descending_order(int5))
print('\n')

