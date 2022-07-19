def hero(bullets, dragons):
    if (bullets / 2) >= dragons:
        print('You live')
        return True
    else:
        print('You die')
        return False


hero(10, 5)
hero(5, 1)
hero(10, 6)
hero(25, 9)
