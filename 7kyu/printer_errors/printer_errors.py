import re


def printer_error(s):
    length_of_s = len(s)
    illegal_chars = []
    for each in s:
        match = re.search(r'[a-m]', each)
        if not match:
            illegal_chars.append(each)
    # print(illegal_chars)
    how_many_errors = len(illegal_chars)
    return "%s/%s" % (how_many_errors, length_of_s)



# test variables
s1 = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
s2 = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
s3 = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
s4 = "aaaaaaaaaaaaaaaabbbbbbbb  bbbbbbbb&*bbmmmmmmmmm$@  mmmmmmmmmmxyz"
s5 = "aaaaaaaaaaaa!@#$%^aaaabbbbbbbbbbbbbbbbbbm)*&%$@mmmmmmmmmmmmmmmmmmxyz"
s6 = "aaaaaaaaaaaaaaaabbbbbbbbbbbb11728395056bbbbbbmmmmmmmmmmmmmmmmmmmxyz"
s7 = 'abcdef!@#$xyz'
s8 = 'abcdef!@#$xyz '

print(printer_error(s1))
print(printer_error(s2))
print(printer_error(s3))
print(printer_error(s4))
print(printer_error(s5))
print(printer_error(s6))
print(printer_error(s7))
print(printer_error(s8))
