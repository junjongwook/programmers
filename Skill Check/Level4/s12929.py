# -*- coding: utf-8 -*-
"""
올바른 괄호의 갯수 : https://programmers.co.kr/learn/courses/30/lessons/12929?language=python3
"""

answer = 0
def solution(n):

    def DFS(arr):
        global answer
        if len(arr) == n * 2:
            # print(f'arr = {arr}')
            answer = answer + 1
            return

        plusCount = arr.count(1)
        minusCount = arr.count(-1)

        if plusCount < n:
            DFS(arr + [1])

        if minusCount < n and sum(arr) > 0:
            DFS(arr + [-1])

    DFS([])

    return answer


if __name__ == '__main__':
    # result = solution(2)
    # print(f'result = {result}')
    # assert result == 2

    result = solution(3)
    print(f'result = {result}')
    assert result == 5