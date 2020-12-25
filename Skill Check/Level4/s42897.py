# -*- coding: utf-8 -*-
"""
도둑질 : https://programmers.co.kr/learn/courses/30/lessons/42897
"""


def solution(money):
    answer = 0
    width = len(money)
    dp = [[0] * width, [0] * width]
    dp[0][0] = 0
    dp[1][0] = money[0]
    # print(*dp, sep='\n')
    for i in range(1, width):
        dp[0][i]= max(dp[0][i-1], dp[1][i-1])
        dp[1][i] = dp[0][i-1] + money[i]
        # print(*dp, sep='\n')

    if width % 2 == 2:
        answer = max(dp[0][width-1], dp[1][width-1])
    else:
        answer = dp[0][width-1]

    return answer


if __name__ == '__main__':
    result = solution([1, 2, 3, 1])
    print(f'result = {result}')
    assert result == 4
