"""
no story, just make this
write function accum
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(s):
    how_many = len(s)
    accum_container = []
    each_set = []
    final_set = []
    func_counter = 1
    for each in s:
        each_times = each * func_counter
        func_counter += 1
        each_set.append(each_times)
    for i in each_set:
        first_let_cap = i.capitalize()
        final_set.append(first_let_cap)
    func_to_string = ''
    for x in final_set:
        func_to_string += '-' + x
    remove_first = func_to_string[1:]
    return remove_first


test1 = "abcd"
test2 = "RqaEzty"
test3 = "cwAt"

print(test1)
print(accum(test1))
print(test2)
print(accum(test2))
print(test3)
print(accum(test3))

