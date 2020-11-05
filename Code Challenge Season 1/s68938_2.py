# -*- coding: utf-8 -*-
'''
문자열의 아름다움

'''

def solution(s):
    answer = -1
    size = len(s)
    temp = [[0] * size for _ in range(size)]

    for i in range(1, size):
        for j in range(0, size - i):
            # print((j, i + j))
            if s[j] != s[i + j]:
                temp[j][i + j] = i
            else:
                temp[j][i + j] = max(temp[j+1][i + j], temp[j][i + j - 1])

    answer = sum([sum(t) for t in temp])

    return answer




if __name__ == '__main__':
    result = solution("baby")
    print(f'result = {result}')
    assert result == 9

    result = solution("oo")
    print(f'result = {result}')
    assert result == 0