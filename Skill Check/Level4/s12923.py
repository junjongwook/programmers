# -*- coding: utf-8 -*-
"""
숫자블록 : https://programmers.co.kr/learn/courses/30/lessons/12923?language=python3
"""


def solution(begin, end):
    answer = []

    def block(num):
        if num == 1: return 0
        for d in range(2, num+1):
            q, r = divmod(num, d)
            if r == 0:
                return q
        return 0

    for n in range(begin, end+1):
        answer.append(block(n))

    return answer


if __name__ == '__main__':
    result = solution(1, 10)
    print(f'result = {result}')
    assert result == [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]