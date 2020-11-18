# -*- coding: utf-8 -*-
"""
점프와 순간 이동 : https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
"""


def solution(n):
    if n == 1: return 1
    ans = solution(n // 2) + (n % 2)
    return ans


if __name__ == '__main__':
    result = solution(5)
    print(f'result = {result}')
    assert result == 2

    result = solution(5000)
    print(f'result = {result}')
    assert result == 5
