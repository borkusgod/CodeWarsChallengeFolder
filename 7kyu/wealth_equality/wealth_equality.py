def redistribute_wealth(wealth):
    # handling presets
    if wealth == [0]:
        return 0
    if len(wealth) == 1:
        return None
    print(wealth)
    get_len = len(wealth)
    # print(f'The len of the list: {get_len}')

    # check if list is already averaged
    result = all(each == wealth[0] for each in wealth)
    if result:
        print('All list items are already averaged')
        return wealth
    else:
        # logic for averaging list
        # print('Not all equal')
        add_container = 0
        new_list = []
        for each in wealth:
            add_container += each
        # print(add_container)
        each_el = add_container / get_len
        # print(type(each_el))
        # print(each_el)
        conv_str = str(each_el)
        print(conv_str)
        x = conv_str.split('.')
        if x[1] == '0':
            print('each_el is a even decimal')
            conv2int = int(each_el)
            each_el = conv2int
        for each in range(get_len):
            new_list.append(each_el)
        wealth = new_list
        return wealth


arr1 = [5, 5, 5, 5, 5]
arr2 = [0, 10]
arr3 = [5]
arr4 = [3, 2, 2]
arr5 = [0]

print(redistribute_wealth(arr1))
print('\n')

print(redistribute_wealth(arr2))
print('\n')

print(redistribute_wealth(arr3))
print('\n')

print(redistribute_wealth(arr4))
print('\n')

print(redistribute_wealth(arr5))
print('\n')

'''
n0v4s3c — Today at 7:01 PM
In c++ you would pass the argument by reference to modify to the original array. 
In python, I think you use [:] so in your function do this
wealth[:] = modifiedList
Where modifiedList is your modified list.

n0v4s3c — Today at 7:12 PM
/run python
l = [5, 6, 10]

def redistribute(wealth):
    wealth[:] = [sum(wealth)/len(wealth) for i in range(len(wealth))]

redistribute(l)  
print(l)

'''
