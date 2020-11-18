# -*- coding: utf-8 -*-
"""
예상 대진표 : https://programmers.co.kr/learn/courses/30/lessons/12985?language=python
"""


def solution(n, a, b):
    answer = 1
    a, b = min(a, b), max(a, b)
    while True:
        if a % 2 == 1 and a + 1 == b:
            break
        else:
            a = (a + 1) // 2
            b = (b + 1) // 2
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution(8, 4, 7)
    print(f'result = {result}')
    assert result == 3

