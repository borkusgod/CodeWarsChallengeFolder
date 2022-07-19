

def validate_pin(pin):
    how_long = len(pin)
    if how_long == 4 or how_long == 6:
        from_each = []
        for each in pin:
            if not each.isdigit():
                print(each)
                return False
                # return False
            if each.isdigit():
                from_each.append(each)
            print(from_each)
        if len(from_each) == how_long:
            return True
    else:
        return False


pin001 = '1234'
pin002 = '123456'
pin003 = '12345'
pin004 = 'a1234'
pin005 = 'a12345'
pin006 = 'abcd12'
pin007 = '1'
pin008 = '12'
pin009 = '1234567'
pin010 = '-12345'
pin011 = '1.234'
pin012 = '12.0'
pin013 = '1234.0'
pin014 = '123      '
pin015 = '111-'
pin016 = '44444-'
pin017 = '123/'

# print(bool(validate_pin(pin001)))
print('pin001')
print(validate_pin(pin001))
print('\n')
print('pin002')
print(validate_pin(pin002))
print('\n')
print('pin003')
print(validate_pin(pin003))
print('\n')
print('pin004')
print(validate_pin(pin004))
print('\n')
print('pin005')
print(validate_pin(pin005))
print('\n')
print('pin006')
print(validate_pin(pin006))
print('\n')
print('pin007')
print(validate_pin(pin007))
print('\n')
print('pin008')
print(validate_pin(pin008))
print('\n')
print('pin009')
print(validate_pin(pin009))
print('\n')
print('pin010')
print(validate_pin(pin010))
print('\n')
print('pin011')
print(validate_pin(pin011))
print('\n')
print('pin012')
print(validate_pin(pin012))
print('\n')
print('pin013')
print(validate_pin(pin013))
print('\n')
print('pin014')
print(validate_pin(pin014))
print('\n')
print('pin015')
print(validate_pin(pin015))
print('\n')
print('pin016')
print(validate_pin(pin016))
print('\n')
print('pin017')
print(validate_pin(pin017))
