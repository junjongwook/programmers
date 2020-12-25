# -*- coding: utf-8 -*-
"""
짝수 행 세기 : https://programmers.co.kr/learn/courses/30/lessons/68647?language=python3
"""
from math import factorial

CDict = dict()
def solution(a):
    answer = 0
    cols = len(a[0])
    rows = len(a)
    f = [[0] * (rows + 1) for _ in range(cols)]

    def C(n, r):
        if (n, r) in CDict:
            return CDict[(n, r)]
        _n = factorial(n)
        _r1 = factorial(r)
        _r2 = factorial(n-r)
        CDict[(n, r)] = _n // (_r1 * _r2)

        return CDict[(n, r)]

    def getOneCount(c):
        _count = 0
        for i in range(rows):
            if a[i][c] == 1: _count += 1
        return _count

    def getZeroCount(c):
        _count = 0
        for i in range(rows):
            if a[i][c] == 0: _count += 1
        return _count

    evenCount = getZeroCount(0)
    f[0][evenCount] = C(rows, evenCount)

    for i in range(1, cols):
        oneCount = getOneCount(i)
        if oneCount == 0:
            f[i] = f[i-1][:]
            continue
        if oneCount == rows:
            f[i] = list(reversed(f[i-1]))
            continue
        for j in range(rows + 1):
            if f[i-1][j] == 0: continue
            for o in range(0, oneCount + 1):
                if j < o: continue
                if (rows - j) < (oneCount - o): continue
                target = j - o + (oneCount - o)     # 짝수행을 o 개만큼 없애고, 홀수행을 oneCount - o 만큼 없애기
                f[i][target] += f[i-1][j] * C(j, o) * C(rows - j, oneCount - o)
                f[i][target] %= 10_000_019

    # print(*f, sep='\n')
    answer = f[-1][-1]

    return answer

if __name__ == '__main__':
    # result = solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])
    # print(f'result = {result}')
    # assert result == 6
    #
    # result = solution([[1,0,0],[1,0,0]])
    # print(f'result = {result}')
    # assert result == 0

    result = solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]])
    print(f'result = {result}')
    assert result == 72

