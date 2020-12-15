# -*- coding: utf-8 -*-
"""
N으로 표현 : https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
"""


def solution(N, number):
    if N == number: return 1
    nDict = dict()
    nDict[1] = {N}
    nDict[2] = {N + N, N - N, N * N, N / N, int(str(N) * 2)}
    if number in nDict[2]:
        return 2

    for i in range(3, 9):
        temp = {int(str(N) * i)}
        if number in temp:
            return i
        for j in range(1, i//2 + 1):
            j2 = i - j
            for n1 in nDict[j]:
                for n2 in nDict[j2]:
                    _n = n1 + n2
                    if _n == number: return i
                    temp.add(_n)
                    _n = n1 - n2
                    if _n == number: return i
                    temp.add(_n)
                    _n = n1 * n2
                    if _n == number: return i
                    temp.add(_n)
                    if n2 != 0:
                        _n = n1 / n2
                        if _n == number: return i
                        temp.add(_n)
                    if n1 != 0:
                        _n = n2 / n1
                        if _n == number: return i
                        temp.add(_n)
        nDict[i] = temp

    return -1


if __name__ == '__main__':
    result = solution(5, 12)
    print(f'result = {result}')
    assert result == 4