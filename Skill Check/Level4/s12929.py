# -*- coding: utf-8 -*-
"""
올바른 괄호의 갯수 : https://programmers.co.kr/learn/courses/30/lessons/12929?language=python3
"""

answer = 0
def solution(n):

    def DFS(arr, p, m):
        global answer
        if len(arr) == n * 2:
            # print(f'arr = {arr}')
            answer = answer + 1
            return

        if p < n:
            DFS(arr + [1], p + 1, m)

        if m < n and sum(arr) > 0:
            DFS(arr + [-1], p, m + 1)

    DFS([], 0, 0)

    return answer


if __name__ == '__main__':
    # result = solution(2)
    # print(f'result = {result}')
    # assert result == 2

    result = solution(3)
    print(f'result = {result}')
    assert result == 5