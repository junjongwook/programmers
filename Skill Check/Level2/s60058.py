# -*- coding: utf-8 -*-
'''
괄호 변환 : https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
'''


def isCorrect(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif count > 0:
            count -= 1
        else:
            return False

    return True


def divide(s):
    u, v = '', ''
    if s == '': return u, v
    count = 1 if s[0] == '(' else -1
    for i in range(1, len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return s[:i+1], s[i+1:]
    else:
        return s, ''


def solution(p):
    if p == '': return ''
    answer = ''
    u, v = divide(p)
    if isCorrect(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        answer += ''.join(['(' if _u == ')' else ')' for _u in list(u[1:-1])])

    return answer


if __name__ == '__main__':
    # result = solution("(()())()")
    # print(f'result = {result}')
    # assert result == "(()())()"
    #
    # result = solution(")(")
    # print(f'result = {result}')
    # assert result == "()"


    result = solution("()))((()")
    print(f'result = {result}')
    assert result == "()(())()"

# print(isCorrect("(()())()"))
    # print(divide("(()())()"))