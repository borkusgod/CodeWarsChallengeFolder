# in this kata, you are asked to square every digit of a number and
# concatenate them. For example, if we run 9119 through the function, 811181
# will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    from_input = str(num)
    string_container = ''
    for each in from_input:
        back2num = int(each)
        each_squared = back2num ** 2
        back2string = str(each_squared)
        string_container += back2string
    return int(string_container)


print(square_digits(9119))

