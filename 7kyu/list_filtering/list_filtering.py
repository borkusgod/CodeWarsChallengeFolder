def filter_list(l):
    print(l)
    container_list = []
    for each in l:
        print(each)
        if isinstance(each, int):
            container_list.append(each)
    return container_list


list1 = [1, 2, 'a', 'b']
list2 = [1, 'a', 'b', 0, 15]
list3 = [1, 2, 'aasf', '1', '123', 123]

print(filter_list(list1))
print('\n')
print(filter_list(list2))
print('\n')
print(filter_list(list3))
print('\n')

