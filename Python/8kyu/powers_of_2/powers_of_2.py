def powers_of_two(n):
    container_list = []
    for_count = n + 1
    print(f'for counting {for_count}')
    for each in range(for_count):
        get_power = 2 ** each
        # print(type(get_power))
        print(f'2 to the n power is: {get_power}')
        container_list.append(get_power)
    return container_list


print(powers_of_two(0))
print('\n')
print(powers_of_two(1))
print('\n')
print(powers_of_two(2))
