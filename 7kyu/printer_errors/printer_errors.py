"""
In a factory a printer labels for boxes. For one kind of boxes the printer
has to use colors which, for the sake of simplicity, are named with letters
from a to m. The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm meaing that the
printer used three times color a, four time color b, one time color h then
one time color a. Sometimes there are problems: lack of colors, technical
malfunction and a "bad" control string is produced e.g.
aaaxbbbbyyhwawiwjjjwwm with the letters not from a to m. You have to write a
function printer_error which given a string will return the error rate of the
printer as a string representing a rational whose numerator is the number of
errors and the denominator the lenght of the control string. Don't reduce this
fraction to a simpler expression.
The string has a length greater or equal to one and contains only letters
from a to m.
examples:
s = 'aaabbbbhaijjjm'
printer_error(s) => "0/14"

s = 'aaaxbbbbyyhwawiwjjjwwm'
printer_error(s) => "8/22"
"""
# instructions and examples
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
