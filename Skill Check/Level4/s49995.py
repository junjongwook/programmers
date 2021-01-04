# -*- coding: utf-8 -*-
"""
쿠키 구입 : https://programmers.co.kr/learn/courses/30/lessons/49995?language=python3
"""


def solution(cookie):
    answer = 0
    cookieSum = [0]
    for c in cookie:
        cookieSum.append(cookieSum[-1] + c)

    l, r = 1, len(cookieSum) - 1

    while l < r:
        total = cookieSum[r] - cookieSum[l-1]
        if total % 2 == 1:      # 전체 합이 짝수가 아니면 계산할 필요 없다.
            if cookie[l-1] > cookie[r-1]:
                r = r - 1
            else:
                l = l + 1
            continue
        for m in range(l, r):
            first = cookieSum[m] - cookieSum[l-1]
            if first * 2 == total:
                return first
        if cookie[l-1] > cookie[r-1]:
            r = r - 1
        else:
            l = l + 1

    return answer


if __name__ == '__main__':
    result = solution([1,1,2,3])
    print(f'result = {result}')
    assert result == 3

    result = solution([1, 2, 4, 5])
    print(f'result = {result}')
    assert result == 0