def is_divisible(n,x,y):
    if (n % x) == 0 and (n % y) == 0:
        # return f'true because {n} is divisible by {x} and {y}'
        return True
    elif (n % x) != 0:
        # return f'false because {n} is not divisible by {x}'
        return False
    elif (n % y) != 0:
        # return f'false because {n} is not divisible by {y}'
        return False
    else:
        # return f'false because {n} is neither divisible by {x} nor {y}'
        return False


print(is_divisible(10, 2, 5))
print(is_divisible(10, 3, 5))
print(is_divisible(10, 2, 7))
print(is_divisible(10, 3, 6))

