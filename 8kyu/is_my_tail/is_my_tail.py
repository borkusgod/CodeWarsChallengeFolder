# def correct_tail(body, tail):
#     sub = body.substr(len(body) - len(tail.length)
#                       if sub = tai:
#     return True
#     else:
#     return False
# original mess from above


def correct_tail(body, tail):
    if body[-1] == tail[0]:
        print('There is a match')
        return True
    else:
        return False



correct_tail('bat', 'lion')
correct_tail('elephant', 'tiger')
correct_tail('niol', 'lion')
correct_tail('cheetah', 'puma')
