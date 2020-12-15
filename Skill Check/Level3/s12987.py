# -*- coding: utf-8 -*-
"""
숫자 게임 : https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3
"""

from bisect import bisect_right

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    for i in range(N):
        a = A[i]
        l = bisect_right(B, a)
        if l == len(B):
            b = B[0]
        else:
            b = B[l]
        if a < b:
            answer = answer + 1
        B.remove(b)

    return answer


if __name__ == '__main__':
    result = solution([5, 1, 3, 7], [2, 2, 6, 8])
    print(f'result = {result}')
    assert result == 3

    result = solution([2,2,2,2], [1,1,1,1])
    print(f'result = {result}')
    assert result == 0

