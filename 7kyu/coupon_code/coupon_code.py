import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    code_check = True
    date_check = True
    invalid_types = ['0', True, False]
    if entered_code in invalid_types or correct_code in invalid_types:
        code_check = False

    if entered_code != correct_code:
        code_check = False
    x = datetime.datetime.now()

    # print(x)
    # print(current_date)
    # print(expiration_date)
    # make function to extract data from dates to convert to ints

    def extract_data(from_input):
        container = []
        split_in_2 = from_input.split(', ')
        for each in split_in_2:
            if ' ' in each:
                spl_again = each.split(' ')
                for each_el in spl_again:
                    container.append(each_el)
            else:
                container.append(each)
        return container

    def month2num(from_input):
        months = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12
        }
        a = from_input.strip()[:3].lower()
        try:
            ez = months[a]
            return ez
        except:
            raise ValueError('Not a month')

    cur_num = extract_data(current_date)
    cur_mon_conv = month2num(cur_num[0])
    # current to ints
    cur_mtn = int(cur_mon_conv)
    cur_day = int(cur_num[1])
    cur_year = int(cur_num[2])
    # print(cur_mtn, cur_day, cur_year)
    x = datetime.datetime(cur_year, cur_mtn, cur_day)
    # print(f'current output: {x}')

    exp_num = extract_data(expiration_date)
    exp_mon_conv = month2num(exp_num[0])
    exp_mtn = int(exp_mon_conv)
    exp_day = int(exp_num[1])
    exp_year = int(exp_num[2])
    # print(exp_mtn, exp_day, exp_year)
    y = datetime.datetime(exp_year, exp_mtn, exp_day)
    # print(f'Expired output: {y}')

    if x > y:
        # print('coupon expired')
        date_check = False

    if not date_check or not code_check:
        return False
    else:
        return True


print('first run')
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))
print('\n')

print('second run')
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))
print('\n')

print('third run')
print(check_coupon("123", "124", "July 2, 2015", "July 2, 2015"))
print('\n')

print('fourth run')
print(check_coupon("123", "123", "January 1, 2015", "July 2, 2015"))
print('\n')

print('fifth run')
print(check_coupon("123", "123", "July 2, 2015", "July 2, 2014"))
print('\n')

print('sixth run')
print(check_coupon("123a", "123", "July 2, 2015", "July 2, 2015"))
print('\n')
