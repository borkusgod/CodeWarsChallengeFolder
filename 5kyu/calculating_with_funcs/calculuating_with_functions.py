"""
This time we want to write calculations using functions
and get the results. Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

"""


def zero(f = None):
    if not f:
        return 1
    else:
        return f(1)


def one(f = None):
    if not f:
        return 1
    else:
        return f(1)


def two(f = None):
    if not f:
        return 1
    else:
        return f(1)


def three(f = None):
    if not f:
        return 1
    else:
        return f(1)


def four(f = None):
    if not f:
        return 1
    else:
        return f(1)


def five(f = None):
    if not f:
        return 1
    else:
        return f(1)


def six(f = None):
    if not f:
        return 1
    else:
        return f(1)


def seven(f = None):
    if not f:
        return 1
    else:
        return f(1)


def eight(f = None):
    if not f:
        return 1
    else:
        return f(1)


def nine(f = None):
    if not f:
        return 1
    else:
        return f(1)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x / y



