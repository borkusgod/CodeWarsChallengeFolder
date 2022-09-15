def splitter(from_input):
    if isinstance(from_input, list):
        for each in from_input:
            print(each)
    # top = ''
    # bot = ''
    # split_each = from_input.split('/')
    # top = split_each[0]
    # bot = split_each[1]
    # return top, bot


list_test = ['160/110']

# print(splitter(list_test))

splitter(list_test)