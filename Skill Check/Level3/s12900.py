# -*- coding: utf-8 -*-
"""
2 x n 타일링 : https://programmers.co.kr/learn/courses/30/lessons/12900
"""


def solution(n):
    if n == 1: return 1
    elif n == 2: return 2

    answer = 0
    from collections import deque
    queue = deque([1, 2])
    for _n in range(3, n+1):
        answer = queue[0] + queue[1]
        answer = answer % 1_000_000_007
        queue.popleft()
        queue.append(answer)

    return answer


if __name__ == '__main__':
    result = solution(4)
    print(f'result = {result}')
    assert result == 5