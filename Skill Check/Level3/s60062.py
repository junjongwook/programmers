# -*- coding: utf-8 -*-
"""
외벽 점검 : https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3
"""

from collections import deque
from itertools import permutations
from bisect import  bisect_right

def revision(numbers, n):
    base = numbers[0]
    return [x - base if x - base >= 0 else x - base + n for x in numbers]

def solution(n, weak, dist):
    answer = n + 1
    weak = deque(weak)
    weakList = []
    for i in range(len(weak)):
        a = deque(weak.copy())
        a = revision(a, n)
        weakList.append(a)
        weak.rotate()

    fList = list(permutations(dist))
    fList.reverse()

    for f in fList:
        for w in weakList:
            _w = w.copy()
            for i, _f in enumerate(f, 1):
                if answer <= i: break
                p = bisect_right(_w, _f)
                if p == len(_w):
                    if i < answer:
                        answer = i
                        continue
                else:
                    _w = _w[p:]
                    _w = revision(_w, n)

    if answer == n + 1: answer = -1

    return answer


if __name__ == '__main__':
    result = solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
    print(f'result = {result}')
    assert result == 2

    result = solution(200, [0, 100], [1, 1])
    print(f'result = {result}')
    assert result == 2

    result = solution(12, [0, 10], [1, 2])
    print(f'result = {result}')
    assert result == 1

    result = solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])
    print(f'result = {result}')
    assert result == 3
