# -*- coding: utf-8 -*-
"""
거스름돈 : https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3
"""


def solution(n, money):
    if n == 0: return 1
    answer = 0
    dp = [[0] * (n+1) for _ in range(len(money))]
    money.sort()
    for i in range(0, n+1):
        dp[0][i] = 1 if i % money[0] == 0 else 0

    for i in range(1, len(money)):
        m = money[i]
        for j in range(m):
            dp[i][j] = dp[i-1][j]
        for j in range(m, n + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-m]) % 1_000_000_007

    answer = dp[-1][-1]

    return answer


if __name__ == '__main__':
    result = solution(5, [1, 2, 5])
    print(f'result = {result}')
    assert result == 4

