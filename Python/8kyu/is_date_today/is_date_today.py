from datetime import datetime


def is_today(date):
    from_input = date
    cust_ = from_input.strftime("%B, %d, %I, %M")
    print(f'After formatting: {cust_}')
    right_now = datetime.today()
    today_form = right_now.strftime("%B, %d, %I, %M")
    print(today_form)
    if cust_ == today_form:
        print(True)
        return True
    else:
        print(False)
        return False


x = datetime(2020, 10, 1, 1, 1, 1, 1)
y = datetime(2080, 10, 1, 1, 1, 1, 1)
z = datetime.today()

is_today(x)
print('\n')
is_today(y)
print('\n')
is_today(z)

