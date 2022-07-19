def divisors(integer):
    print(integer)
    if integer == 0:
        return 0
    container = []
    for each in range(integer + 1):
        # print(each)
        if each > 1:
            if (integer % each) == 0:
                container.append(each)
    if len(container) == 1:
        return f'{integer} is prime'
    else:
        container.pop()
        return container


test_number1 = 15
test_number2 = 253
test_number3 = 24
test_number4 = 25
test_number5 = 13
test_number6 = 3
test_number7 = 29

print(divisors(test_number1))
print('\n')
print(divisors(test_number2))
print('\n')
print(divisors(test_number3))
print('\n')
print(divisors(test_number4))
print('\n')
print(divisors(test_number5))
print('\n')
print(divisors(test_number6))
print('\n')
print(divisors(test_number7))
print('\n')
