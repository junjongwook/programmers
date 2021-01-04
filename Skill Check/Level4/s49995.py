# -*- coding: utf-8 -*-
"""
쿠키 구입 : https://programmers.co.kr/learn/courses/30/lessons/49995?language=python3
"""


def solution(cookie):
    answer = 0
    cookieSum = [0] # prefix Sum 을 이용하기 위한 sum array
    for c in cookie:
        cookieSum.append(cookieSum[-1] + c)

    l, r = 1, len(cookieSum) - 1

    for l in range(1, len(cookieSum) - 1):
        for r in range(len(cookieSum) - 1, l, -1):
            total = cookieSum[r] - cookieSum[l-1]
            if total <= answer * 2:             # 앞서 나온 결과보다 작은 거라면 그냥 통과다
                break
            if total % 2 == 1: continue         # 총합이 홀수면 2개로 똑같이 못 나눈다.
            for m in range(l, r):
                first = cookieSum[m] - cookieSum[l-1]
                if first * 2 == total and answer < first:
                    answer = first

    return answer


if __name__ == '__main__':
    result = solution([1,1,2,3])
    print(f'result = {result}')
    assert result == 3

    result = solution([1, 2, 4, 5])
    print(f'result = {result}')
    assert result == 0