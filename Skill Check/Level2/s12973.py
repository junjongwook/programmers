# -*- coding: utf-8 -*-
"""
짝지어 제거하기 : https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
"""
from collections import deque


def solution(s):
    queue = deque(s)
    queue2 = deque([])
    while queue:
        q = queue.popleft()
        if len(queue2) == 0 or queue2[-1] != q:
            queue2.append(q)
        else:
            p = queue2.pop()
    if len(queue2) > 0: return 0
    else: return 1


if __name__ == '__main__':
    result = solution("baabaa")
    print(f'result = {result}')
    assert result == 1

    result = solution("cdcd")
    print(f'result = {result}')
    assert result == 0
