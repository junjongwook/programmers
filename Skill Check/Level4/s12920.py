# -*- coding: utf-8 -*-
"""
선입 선출 스케쥴링 : https://programmers.co.kr/learn/courses/30/lessons/12920?language=python3
"""
from math import gcd
from functools import reduce


def solution(n, cores):
    answer = 0
    N = len(cores)

    '''
    이게 시간이 많이 걸리려나? 이걸 삭제하고 해보자.
    def lcm(x, y, /):
        return x * y // gcd(x, y)

    _lcm = reduce(lcm, cores)
    temp = 0
    for i in range(N):
        temp += _lcm // cores[i]

    while n >= temp:
        n -= temp
    '''

    def throughput(t:int, /):   # 시작한 개수로 변경 (완료 기준이 아니다)
        total = 0
        for core in cores:
            q, r = divmod(t, core)
            total += q
            if r > 0: total += 1

        return total

    left, right = 0, n * cores[0]
    later = 0
    l = 0
    r = throughput(right)
    while left < right:
        mid = (left + right) // 2
        t = throughput(mid)
        # print(f'left = {left}, right = {right}, mid = {mid}, t = {t}')
        if t < n:
            later = mid
            left = mid + 1
            l = throughput(left)
        else:
            right = mid - 1
            r = throughput(right)

    # print(f'later = {later}')
    # later time 시점이전까지의 process 진행 상황을 확인하고
    # process 상의 상태를 만든다.
    n = n - throughput(later)   # 이미 완료되어서 없어진 대상
    process = [0] * N
    target = []
    for i in range(N):
        p = later % cores[i]
        if p == 0:
            target.append(i)
        else:
            process[i] = cores[i] - p

    # print(f'process = {process}')
    # print(f'target = {target}')
    # print(f'n = {n}')

    while n > 0:
        for i in target:
            process[i] = cores[i]
            n = n - 1
            if n == 0:
                return i + 1
        # 시간을 한번 흘려 보냄
        _min = min(process)
        target = []
        for i in range(N):
            process[i] -= _min
            if process[i] == 0:
                target.append(i)

    return answer


if __name__ == '__main__':
    result = solution(6, [1,2,3])
    print(f'result = {result}')
    assert result == 2
