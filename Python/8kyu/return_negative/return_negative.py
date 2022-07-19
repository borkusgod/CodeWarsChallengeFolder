def make_negative( number ):
    if number == 0:
        return 0
    else:
        return -abs(number)


print(make_negative(5))
print(make_negative(-5))
print(make_negative(0))