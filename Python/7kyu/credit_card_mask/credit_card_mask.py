# return masked string
def maskify(cc):
    print(cc)
    to_string = str(cc)
    to_mask = to_string[1:-3]
    masked = ''
    for each in to_mask:
        x = each.replace(each, '#')
        masked = masked + x
    unmasked = to_string[-4:]
    final = masked + unmasked
    return final





cc1 = 4450500016172487
cc2 = 4450008092914556
string_test1 = 'reeeeeaaaaaaalllllllllyyyyyyyyyyyyyy'
string_test2 = 'skippyTheSpaceCowboy'

print(maskify(cc1))
print('\n')
print(maskify(cc2))
print('\n')
print(maskify(string_test1))
print('\n')
print(maskify(string_test2))
print('\n')

