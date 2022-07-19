def capital(capitals):
    empty_container = []
    # print(empty_container)
    for each in capitals:
        into_dict = each
        find_st_cntr = into_dict.get('country') or into_dict.get('state')
        find_capital = into_dict.get('capital')
        y = 'The capital of {} is {}'.format(find_st_cntr, find_capital)
        # print(y)
        empty_container.append(y)
    return empty_container


from_input = [{'state': 'Maine', 'capital': 'Augusta'}]
# print(from_input[0])
from_input2 = [{"state": 'Maine', 'capital': 'Augusta'},
               {'country': 'Spain', "capital": "Madrid"}]
# print(from_input2[1])
print(capital(from_input))
print(capital(from_input2))
#
# for i in from_input:
#     from_list = i
#     print(from_list)
#     find_cap = from_list.get('capital')
#     print(find_cap)




