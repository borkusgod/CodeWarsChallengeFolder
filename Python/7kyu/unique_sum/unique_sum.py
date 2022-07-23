def unique_sum(lst):
    return sum(set(lst)) if lst else None


list1 = [1, 2, 3]
list2 = [1, 3, 8, 1, 8]
list3 = [-1, -1, 5, 2, -7]

print(unique_sum(list1))
print(unique_sum(list2))
print(unique_sum(list3))

