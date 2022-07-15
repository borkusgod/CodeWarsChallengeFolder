def sorter(textbooks):
    #Cramming before a test can't be that bad?
    print(textbooks)
    textbooks.sort()
    print(textbooks)


list1 = [['Algebra', 'History', 'Geometry', 'English'],
            ['Algebra', 'English', 'Geometry', 'History']]
list2 = [['Algebra', 'history', 'Geometry', 'english'],
            ['Algebra', 'english', 'Geometry', 'history']]
list3 = [['Alg#bra', '$istory', 'Geom^try', '**english'],
            ['$istory', '**english', 'Alg#bra', 'Geom^try']]

print(sorter(list1))
print('\n')
print(sorter(list2))
print('\n')
print(sorter(list3))
print('\n')
