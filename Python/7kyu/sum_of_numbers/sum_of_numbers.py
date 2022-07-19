def get_sum(a,b):
    if a == b:
        return a
    s = 0
    for n in range(min(a, b), max(a, b)+1):
        s += n
    return s


print(get_sum(1, 0))
print('\n')
print(get_sum(-5, 8))
print('\n')
print(get_sum(-1, 4))
print('\n')
print(get_sum(11, 16))
print('\n')
print(get_sum(-1, 0))
print('\n')
print(get_sum(-1, 2))
print('\n')
