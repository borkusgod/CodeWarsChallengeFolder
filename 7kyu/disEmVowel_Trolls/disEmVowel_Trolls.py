"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the
vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return
a new string with all vowels removed. For example, the string "This
website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
"""


def disemvowel(string_):
    print(string_)
    raw_s = f'\"{string_}\"'
    print(raw_s)
    vowel_list = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    split_into_words = string_.split(' ')
    formatted_string = ''
    for each in split_into_words:
        word_formatted = ''
        for letter in each:
            if letter in vowel_list:
                x = letter.replace(letter, '')
                letter = x
            if letter:
                word_formatted += letter
        formatted_string += word_formatted
        formatted_string += ' '
    strip_down = formatted_string.strip()
    return strip_down


string_to_test = 'looking for a string with consonants and vowels.'
string_with_uppers = 'looking For a String that has Uppers and lowers'
randoms = " -zE-JSUzAuEI_u OWIz^CaSoA_VaWeIOMuu?}In< EcXau)eu n@E a  ' \
          'mx*oNU'): '-z-JSz_ Wz^CS_VWM?}n< cX) n@   mx*N"
randoms2 = """
EVzaoFlqcnQBC;~Ou qIez~'AEFw b "): "VzFlqcnQBC;~ qz~'Fw b
"""
# randoms4 = 'iqiOgE?tiOCK[AalOem i'): 'qg?tCK[lm'
# randoms3 = """
# \\oEOXoOWaeo&v,ELFae'): '\\XW&v,LF
# """
# randoms4 = '\\oEOXoOWaeo&v,ELFae'): '\\XW&v,LF'
# remove_vowels(string_to_test)

print(string_to_test)
print(disemvowel(string_to_test))
print(string_with_uppers)
print(disemvowel(string_with_uppers))
# print(disemvowel(randoms))
print(randoms2)
print(disemvowel(randoms2))
# print(randoms3)
# # print(disemvowel(randoms3))
# print(randoms4)
# print(disemvowel(randoms4))
