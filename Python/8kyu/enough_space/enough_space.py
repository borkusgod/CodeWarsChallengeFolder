def enough(cap, on, wait):
    # Your code here
    room_left = (cap - on)
    if wait <= room_left:
        print(f'He can fit all {wait} passengers')
        return 0
    else:
        left_waiting = wait - room_left
        print(f'He couldn\'t fit {left_waiting} of the {wait} waiting')
        return left_waiting


print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))
