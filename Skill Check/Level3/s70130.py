# -*- coding: utf-8 -*-
"""
스타 수열 : https://programmers.co.kr/learn/courses/30/lessons/70130
"""
from collections import Counter

def solution(a):
    width = len(a)
    if width < 2:
        return 0

    cnt = Counter(a)
    # print(f'cnt = {cnt}')

    answer = 0
    for k, v in cnt.items():
        # items 는 순서대로 나오지 않네
        # if answer >= v * 2: break
        prev = None
        temp = []
        for i in range(width):
            if a[i] == k:
                if prev != None and prev != k:
                    temp.append(prev)
                    temp.append(a[i])
                    prev = None
                    continue
            if prev == k:
                if a[i] != k:
                    temp.append(prev)
                    temp.append(a[i])
                    prev = None
                    continue
            prev = a[i]
        # print(f'temp = {temp}')
        answer = max(len(temp), answer)

    return answer


if __name__ == '__main__':
    result = solution([0])
    print(f'result = {result}')
    assert result == 0

    result = solution([5,2,3,3,5,3])
    print(f'result = {result}')
    assert result == 4

    result = solution([0,3,3,0,7,2,0,2,2,0]	)
    print(f'result = {result}')
    assert result == 8

    result = solution([0, 1, 1])
    print(f'result = {result}')
    assert result == 2

    result = solution([0, 1, 2, 3])
    print(f'result = {result}')
    assert result == 2