# convert to int if decimal is 0

a = 5.5
b = 5.0

print(type(b))

temp_conv = str(b)
print(type(temp_conv))

x = temp_conv.split('.')
if x[1] == '0':
    print('true')
    conv_b = int(b)
    b = conv_b

print(type(b))
print(b)
