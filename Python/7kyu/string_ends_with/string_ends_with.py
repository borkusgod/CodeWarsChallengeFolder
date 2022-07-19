def solution(string, ending):
    test = string.endswith(ending)
    if test:
        return True
    else:
        return False


print(solution('abcde', 'cde'))
print('\n')
print(solution('abcde', 'abc'))
print('\n')
print(solution('abcde', ''))
print('\n')
print(solution('cody', 'do'))
print('\n')
print(solution('rainbow', 'bow'))
print('\n')
