def friend(x):
    print(x)
    print(f'There are {len(x)} entries in the list.')
    names_with_4_letters = []
    for each in x:
        if len(each) == 4:
            let_test = each.isalpha()
            if let_test:
                names_with_4_letters.append(each)
    print('The following list is made of names with four characters.')
    return names_with_4_letters


test_samp1 = ["Ryan", "Kieran", "Mark"]
test_samp2 = ["Ryan", "Jimmy", "1234"]
test_samp3 = ["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]

print(friend(test_samp1))
print('\n')
print(friend(test_samp2))
print('\n')
print(friend(test_samp3))
print('\n')

