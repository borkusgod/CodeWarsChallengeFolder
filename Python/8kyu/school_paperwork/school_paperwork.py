def paperwork(n, m):
    if n < 0:
        n = 0
    if m < 0:
        m = 0
    return n * m


# test_list1 = (5, 5)
# test_list2 = (-5, 5)
# test_list3 = (5, -5)
# test_list4 = (-5, -5)
# test_list5 = (5, 0)

print(paperwork(5, 5))
print(paperwork(-5, 5))
print(paperwork(5, -5))
print(paperwork(-5, -5))
print(paperwork(5, 0))
