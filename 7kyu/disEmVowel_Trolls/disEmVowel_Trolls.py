# def disemvowel(string_):
#     str_no_vow = ''
#     vowel_list = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#     find_words = string_.split(' ')
#     # print(find_words)
#     for each in find_words:
#         for each_let in each:
#             if not each_let in vowel_list:
#                 str_no_vow += each_let
#         str_no_vow += ' '
#     print(type(str_no_vow))
#     return str_no_vow

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    # found this solution at: https://www.youtube.com/watch?v=SDbT8rBr8XI
    return ''.join(filter(lambda char: char not in vowels, string_))


test_string1 = 'This website is for losers LOL!'

print(test_string1)
print(disemvowel(test_string1))