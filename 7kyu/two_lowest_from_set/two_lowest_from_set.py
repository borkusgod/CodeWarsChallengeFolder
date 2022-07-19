def sum_two_smallest_numbers(numbers):
    container = 0
    find_min = min(numbers)
    container = container + find_min
    numbers.remove(find_min)
    find_min = min(numbers)
    container = container + find_min

    return container


set1 = [5, 8, 12, 18, 22]
set2 = [7, 15, 12, 18, 22]
set3 = [25, 42, 12, 18, 22]

print(sum_two_smallest_numbers(set1))
print('\n')
print(sum_two_smallest_numbers(set2))
print('\n')
print(sum_two_smallest_numbers(set3))
print('\n')