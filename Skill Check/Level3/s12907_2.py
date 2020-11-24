# -*- coding: utf-8 -*-
"""
거스름돈 : https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3
"""

answer = 0
def solution(n, money):
    if n == 0: return 1
    money.reverse()
    l = len(money)

    def DFS(L, s, i):
        global answer
        if s > n:
            return
        if s == n:
            answer = answer + 1
            # print(f'L = {L}, s = {s}, answer = {answer}')
            return
        for _i in range(i, l):
            DFS(L+1, s+money[_i], _i)

    DFS(0, 0, 0)

    return answer


if __name__ == '__main__':
    result = solution(5, [1, 2, 5])
    print(f'result = {result}')
    assert result == 4

