# -*- coding: utf-8 -*-
"""
3 x n 타일링 : https://programmers.co.kr/learn/courses/30/lessons/12902?language=python3
"""


def solution(n):
    if n % 2 == 1: return 0

    tiling = [0] * (n + 1)
    tiling[0] = 1
    tiling[1] = 0
    tiling[2] = 3
    tiling[3] = 0
    tiling[4] = 11

    for i in range(6, n + 1, 2):
        tiling[i] = tiling[i-2] * 3
        for j in range(2, i - 4 + 1, 2):
            tiling[i] += (2 * tiling[j])
        tiling[i] += 2

        tiling[i] %= 1_000_000_007

    return tiling[n]


if __name__ == '__main__':
    # result = solution(4)
    # print(f'result = {result}')
    # assert result == 11
    #
    # result = solution(6)
    # print(f'result = {result}')
    # assert result == 41

    result = solution(8)
    print(f'result = {result}')
    assert result == 153

