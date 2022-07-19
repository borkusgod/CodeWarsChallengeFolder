def opposite(number):
    if number == 0:
        return 0
    conv2str = str(number)
    if conv2str[0] == '-':
        rmv_neg = conv2str.replace("-", "")
        conv2str = rmv_neg
    else:
        add_neg = "-" + conv2str
        conv2str = add_neg
    if '.' in conv2str:
        return float(conv2str)
    else:
        return int(conv2str)


test_list1 = 1
test_list2 = 25.6
test_list3 = 0
test_list4 = 1425.2222
test_list5 = -3.1458
test_list6 = -95858588225

print(opposite(test_list1))
print(opposite(test_list2))
print(opposite(test_list3))
print(opposite(test_list4))
print(opposite(test_list5))
print(opposite(test_list6))
