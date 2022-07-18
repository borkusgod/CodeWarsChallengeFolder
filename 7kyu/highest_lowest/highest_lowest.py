def high_and_low(numbers):
    list_container = []
    split2_els = numbers.split(' ')
    # print(split2_els)
    for each in split2_els:
        each2int = int(each)
        # print(type(each2int))
        list_container.append(each2int)
    high = max(list_container)
    low = min(list_container)
    # print(high)
    # print(low)
    return f'{high} {low}'


string1 = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

print(high_and_low(string1))

