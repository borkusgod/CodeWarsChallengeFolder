def open_or_senior(data):
    print(data)
    attr_container = []
    for each in data:
        to_list = list(each)
        if to_list[0] < 0:
            to_list[0] = 1
        if to_list[1] < 0:
            to_list[1] = 1
        print(f'Player is {to_list[0]} years old and has a handicap of '
              f'{to_list[1]}')
        if to_list[0] >= 55 and to_list[1] > 7:
            attr_container.append('Senior')
        else:
            attr_container.append('Open')
    print('\n')
    return attr_container


nested_list1 = [(45, 12), (55, 21), (19, -2), (104, 20)]
nested_list2 = [(16, 23), (73, 1), (56, 20), (1, -1)]

print(open_or_senior(nested_list1))
print('\n')
print(open_or_senior(nested_list2))
print('\n')
