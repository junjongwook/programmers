# -*- coding: utf-8 -*-
"""
N으로 표현 : https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
"""

def operator(s1, s2):
    result = set()
    for _s1 in s1:
        for _s2 in s2:
            result.add(_s1 + _s2)
            result.add(_s1 - _s2)
            result.add(_s1 * _s2)
            if _s2 != 0:
                result.add(_s1 // _s2)
    return result


def solution(N, number):
    if N == number: return 1
    answer = -1
    S = [{}, {N}]
    for i in range(2, 9):
        currS = {int(str(N)*i)}
        for op1 in range(1, i):
            op2 = i - op1
            temp = operator(S[op1], S[op2])
            currS.update(temp)

            if number in currS:
                return i
        S.append(currS)

    return answer


if __name__ == '__main__':
    result = solution(5, 12)
    print(f'result = {result}')
    assert result == 4