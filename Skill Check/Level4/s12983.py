# -*- coding: utf-8 -*-
"""
단어 퍼즐 : https://programmers.co.kr/learn/courses/30/lessons/12983?language=python3
"""
from collections import deque


def solution(strs, t):
    answer = -1

    queue = deque([('', 0)])
    while queue:
        s, c = queue.popleft()
        if s == t: return c
        for str in strs:
            _s = s + str
            if t.startswith(_s):
                queue.append((_s, c+1))

    return answer


if __name__ == '__main__':
    result = solution(["ab", "na", "n", "a", "bn"], "nabnabn")
    print(f'result = {result}')
    assert result == 4

    result = solution(["ba", "na", "n", "a"], "banana")
    print(f'result = {result}')
    assert result == 3

    result = solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple")
    print(f'result = {result}')
    assert result == 2

    result = solution(["ba", "an", "nan", "ban", "n"], "banana")
    print(f'result = {result}')
    assert result == -1


