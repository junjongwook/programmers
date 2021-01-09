# -*- coding: utf-8 -*-
"""
무지의 먹방 라이브 : https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
"""
import heapq
from collections import deque

def solution(food_times, k):
    answer = 0
    heap = []
    for i, times in enumerate(food_times, 1):
        heapq.heappush(heap, [times, i])

    prev = 0
    while heap:
        l = len(heap)
        times, i = heapq.heappop(heap)
        if times == prev: continue
        if (times - prev) * l <= k:
            k = k - (times - prev) * l
            prev = times
        else:
            heap.append([times, i])
            break
    else:
        return -1

    heap = [[times - prev, i] for times, i in heap]
    heap.sort(key=lambda x: x[1])
    # print(f'heap = {heap}, k = {k}')
    index = k % len(heap)
    answer = heap[index][1]

    return answer


if __name__ == '__main__':
    result = solution([3, 1, 2], 5)
    print(f'result = {result}')
    assert result == 1

    result = solution([4,2,3,6,7,1,5,8], 16)
    print(f'result = {result}')
    assert result == 3

    result = solution([4,2,3,6,7,1,5,8], 27)
    print(f'result = {result}')
    assert result == 5

    result = solution([1, 1, 1], 10)
    print(f'result = {result}')
    assert result == -1

    result = solution([1, 1, 2], 3)
    print(f'result = {result}')
    assert result == 3

    result = solution([1, 5, 5, 5, 5, 6, 7], 31)
    print(f'result = {result}')
    assert result == 6