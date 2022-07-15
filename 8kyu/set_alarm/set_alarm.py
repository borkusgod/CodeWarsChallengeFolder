def set_alarm(employed, vacation):
    # Your code here
    if employed and vacation:
        return False
    if not employed:
        return False
    if employed and not vacation:
        return True


print(set_alarm(True, True))
print(set_alarm(False, True))
print(set_alarm(False, False))
print(set_alarm(True, False))
