# -*- coding: utf-8 -*-
"""
숫자블록 : https://programmers.co.kr/learn/courses/30/lessons/12923?language=python3
"""


def solution(begin, end):
    answer = [0] * (end - begin + 1)
    maxNum = end // 2

    for n in range(maxNum, 0, -1):
        start = begin // n * n
        start = start + n if start < begin else start
        start = n * 2 if n * 2 > start else start
        for i in range(start, end + 1, n):
            if answer[i - begin] == 0:
                answer[i - begin] = n

    return answer


if __name__ == '__main__':
    result = solution(1, 10)
    print(f'result = {result}')
    assert result == [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]