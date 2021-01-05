# -*- coding: utf-8 -*-
"""
지형 편집 : https://programmers.co.kr/learn/courses/30/lessons/12984?language=python3
"""


def solution(land, P, Q):
    answer = float('inf')
    block = dict()
    N = len(land)
    minH = float('inf')
    maxH = 0
    for i in range(N):
        for j in range(N):
            height = land[i][j]
            minH = min(minH, height)
            maxH = max(maxH, height)
            block.setdefault(height, 0)
            block[height] += 1
    # print(block)

    for h in range(minH, maxH+1):
        _sum = 0
        for _h, _n in block.items():
            if _h > h:
                _sum += (_h - h) * _n * Q
            elif _h < h:
                _sum += (h - _h) * _n * P
        if _sum < answer:
            answer = _sum
        # print(f'h = {h}, _sum = {_sum}')

    return answer


if __name__ == '__main__':
    result = solution([[1, 2], [2, 3]], 3, 2)
    print(f'result = {result}')
    assert result == 5

    result = solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3)
    print(f'result = {result}')
    assert result == 33
