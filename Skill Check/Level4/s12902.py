# -*- coding: utf-8 -*-
"""
3 x n 타일링 : https://programmers.co.kr/learn/courses/30/lessons/12902?language=python3
"""

import sys
sys.setrecursionlimit(10 ** 6)
def solution(n):
    if n < 1: return 1
    if n % 2 == 1: return 0
    if n == 2: return 3

    return solution(n-2) * 3 + solution(n-4) * 2

if __name__ == '__main__':
    result = solution(4)
    print(f'result = {result}')
    assert result == 11