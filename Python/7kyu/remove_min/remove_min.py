def remove_smallest(numbers):
    # make sure to work with copies when possible
    copy_of = numbers.copy()
    print(copy_of)
    if not copy_of:
        return copy_of
    min_from_numbers = min(copy_of)
    print(min_from_numbers)
    copy_of.remove(min_from_numbers)
    return copy_of


list1 = [1, 2, 3, 4, 5]
list2 = [5, 3, 2, 1, 4]
list3 = [1, 2, 3, 1, 1]
list4 = []

print(remove_smallest(list1))
print('\n')
print(remove_smallest(list2))
print('\n')
print(remove_smallest(list3))
print('\n')
print(remove_smallest(list4))
print('\n')
