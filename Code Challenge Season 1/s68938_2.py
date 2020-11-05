# -*- coding: utf-8 -*-
'''
문자열의 아름다움

'''

def solution(s):
    answer = -1
    size = len(s)
    temp = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i >= j: continue
            if s[j] == s[i]:
                temp[i][j] = temp[i][j-1]
            else:
                temp[i][j] = j - i

    answer = sum([sum(t) for t in temp])

    return answer




if __name__ == '__main__':
    result = solution("baby")
    print(f'result = {result}')
    assert result == 9

    result = solution("oo")
    print(f'result = {result}')