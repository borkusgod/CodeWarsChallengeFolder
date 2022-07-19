"""
In this kata, you are given a string for example:
"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well
as the parentheses themselves.
<--------------------
The example above would return:
"exampleexample"
"""
import re


def remove_parentheses(s):
    # result = re.search(r"\(([^\)]+)\)", s)
    s_copy = '' + s
    print(s_copy)
    result = re.findall(r"\(([^\)]+)\)", s)
    # print(result)
    for each in result:
        x = s_copy.replace(each, "")
        print(x)
    print(s_copy)
    # print(s)
    # print(s_copy)


test_list = "fill(inthe)gaps"
test_list2 = "fill(inthe)gaps(withall)theparens"

remove_parentheses(test_list)
remove_parentheses(test_list2)


