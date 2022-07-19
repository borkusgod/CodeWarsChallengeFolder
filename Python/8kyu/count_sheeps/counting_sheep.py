def count_sheeps(sheep):
    empty_container = 0
    for each in sheep:
        if each:
            empty_container = empty_container + each
    return empty_container


array1 = [True,  True, True,  False,
          True,  True, True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

print(count_sheeps(array1))
