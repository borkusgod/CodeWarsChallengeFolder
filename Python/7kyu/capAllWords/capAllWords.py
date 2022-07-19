"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid
(2010) and After Earth (2013). Jaden is also known for some of his philosophy
that he delivers via Twitter. When writing on Twitter, he is known for almost
always capitalizing every word. For simplicity, you'll have to capitalize each
word, check out how contractions are expected to be in the example below.
Your task is to convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith, but they are not capitalized
in the same way he originally typed them.

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""


def to_jaden_case(string):
    # print(string)
    container = ''
    if string == '':
        container = string
    elif string:
        using_split = string.split(' ')
        for each in using_split:
            each_to_lower = each.lower()
            upper_on_word = each_to_lower[0].upper()
            string_list = list(each_to_lower)
            string_list[0] = upper_on_word
            new_string = ''.join(string_list)
            back2string = str(new_string)
            container += back2string
            container += ' '
        strip_whitespace = container.strip()
        return strip_whitespace


long_string = """
UzHBVxCJET IYEkvUIVw ibusCeTt PFMkXoqU josSk aHHEt G jRDzAKnRk 
sbzOKmgJm ihPIg JbtIAIKdZ NITckOcUPz auRv NckSAHB VRWoE k gzpKhOFq 
zoyNcyX mDiYXet XDUwxDMJON yIN p lJWOEME aoznso M uLpbaCh hjt FKM 
aNaLMIwB zng DtiD xAbWIcBzdc uKxmCR ycMSLznaR XtoJqVi g olzpXsuliH 
qsxN Z fkE bkNYUTg wJsSwkrVH HSetP KajrhSQx PMVTBEBF MbmdrRcBS vNaqUrKjY 
yfXsqeO pptrANTuZx SZJXZNU a c gqwzAuD LlIiORHle jiLv lfImPYSqo zOmS QScXGmbdV 
TsBrkZsKf OffqNPJCw OQhkDTF phL BV qE ouaSZuMiy b uAaO ApwNjrLGW LkqJOIq 
YADkRmTxAC fT FT QRxfEAJw NCjdzgEJOg ByEioJSvZ Xuv mhqNwoumd'
"""
print(to_jaden_case(''))
# print(to_jaden_case(long_string))
print(to_jaden_case("test string for printout"))
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))



