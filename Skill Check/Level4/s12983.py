# -*- coding: utf-8 -*-
"""
단어 퍼즐 : https://programmers.co.kr/learn/courses/30/lessons/12983?language=python3
"""


def solution(strs, t):
    N = len(t)
    strs = set(strs)
    _max = 0
    for str in strs:
        _max = max(_max, len(str))

    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for s in range(N):
        end = min(s + _max + 1, N + 1)
        for e in range(s+1, end):
            word = t[s:e]
            # print(f's = {s}, e = {e}, end = {end}, word = {word}')
            if word in strs:
                dp[e] = min(dp[e], dp[s] + 1)
                # print(f's = {s}, e = {e}, dp = {dp}')

    # print(f'dp = {dp}')
    answer = dp[-1] if dp[-1] != float('inf') else -1
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


