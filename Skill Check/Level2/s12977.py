# -*- coding: utf-8 -*-
"""
소수 만들기 : https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
"""


def solution(nums):
    answer = 0

    # 소수 정보를 미리 만들어 둔다.
    primes = [1] * (max(nums) * 3 + 1)
    primes[:2] = [0, 0]
    for i in range(2, len(primes)):
        if primes[i] == 0: continue
        for j in range(i + i, len(primes), i):
            primes[j] = 0

    from itertools import combinations
    targetList = combinations(nums, 3)
    for target in targetList:
        _sum = sum(target)
        if primes[_sum] == 1:
            answer = answer + 1

    return answer


if __name__ == '__main__':
    result = solution([1,2,7,6,4])
    print(f'result = {result}')
    assert result == 4

