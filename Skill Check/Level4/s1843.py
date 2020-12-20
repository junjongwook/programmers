# -*- coding: utf-8 -*-
"""
사칙연산 : https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3
"""

answer = -float('inf')
def solution(arr):
        global answer

        def calc(arr3):
            # print(f'calc arr3 = {arr3}')
            a, op, b = int(arr3[0]), arr3[1], int(arr3[2])
            if op == '+':
                return a + b
            elif op == '-':
                return a - b

        def DFS(arr2):
            # print(f'arr2 = {arr2}')
            global answer
            if len(arr2) == 3:
                answer = max(answer, calc(arr2))
                # print(f'answer = {answer}')
                return

            for i in range(0, len(arr2) - 1, 2):
                # print(f'range arr2 = {arr2}')
                DFS(arr2[:i] + [str(calc(arr2[i:i + 3]))] + arr2[i + 3:])

        DFS(arr)

        return answer


if __name__ == '__main__':
    result = solution(["1", "-", "3", "+", "5", "-", "8"])
    print(f'result = {result}')
    assert result == 1

    result = solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
    print(f'result = {result}')
    assert result == 3