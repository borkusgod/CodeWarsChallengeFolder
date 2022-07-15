"""
simulated atm pin verification. can only be 4 or 6 numbers
can only be numbers
if the function is passed a valid pin string, return true
else return false
"""


def validate_pin(pin):
    how_long = len(pin)
    reorganize_pin = []
    if how_long == 4 or how_long == 6:
        is_pin_num = pin.isdigit()
        if is_pin_num:
            return True
    else:
        return False


# def run_test(from_input):
#     testing = validate_pin(from_input)
#     if testing:
#         print(f'The pin {from_input} is a valid pin.')
#     else:
#         print(f'The pin {from_input} is not valid.')


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


# run_test(pin001)
# run_test(pin002)
# run_test(pin003)
# run_test(pin004)
# run_test(pin005)
# run_test(pin006)
# run_test(pin007)
# run_test(pin008)
# run_test(pin009)
# run_test(pin010)
# run_test(pin011)

print(bool(validate_pin(pin001)))
print(bool(validate_pin(pin002)))
print(bool(validate_pin(pin003)))
print(bool(validate_pin(pin004)))
print(bool(validate_pin(pin005)))
print(bool(validate_pin(pin006)))
print(bool(validate_pin(pin007)))
print(bool(validate_pin(pin008)))
print(bool(validate_pin(pin009)))
print(bool(validate_pin(pin010)))
print(bool(validate_pin(pin011)))




# if validate_pin(pin002):
#     print(f'The pin {pin002} is a valid pin.')
# if validate_pin(pin003):
#     print(f'The pin {pin003} is a valid pin.')
# if validate_pin(pin004):
#     print(f'The pin {pin004} is a valid pin.')
# if validate_pin(pin005):
#     print(f'The pin {pin005} is a valid pin.')
# if validate_pin(pin006):
#     print(f'The pin {pin006} is a valid pin.')



