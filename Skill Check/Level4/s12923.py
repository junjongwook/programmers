# -*- coding: utf-8 -*-
"""
숫자블록 : https://programmers.co.kr/learn/courses/30/lessons/12923?language=python3
"""


def solution(begin, end):
    answer = [1] * (end - begin + 1)

    end2 = int(end ** (1/2))
    for i in range(2, end2 + 1):
        start = max(i * i, (begin + i - 1) // i * i)
        for n in range(start, end + 1, i):
            if answer[n - begin] == 1:
                answer[n - begin] = n // i

    if begin == 1: answer[0] = 0

    return answer


if __name__ == '__main__':
    # result = solution(1, 10)
    # print(f'result = {result}')
    # assert result == [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]

    result = solution(100, 120)
    nums = range(100, 120+1)
    for n, r in zip(nums, result):
        print(f'{n}:{r}', sep=' ')