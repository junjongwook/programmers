# -*- coding: utf-8 -*-
"""
무지의 먹방 라이브 : https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
"""
import heapq


def solution(food_times, k):
    answer = 0
    heap = []
    for i, times in enumerate(food_times, 1):
        heapq.heappush(heap, [times, i])

    prev = 0
    _k = k
    p = 0
    while True:
        l = len(heap)
        t, i = heapq.heappop(heap)
        if prev == t: continue
        if l * (t - prev) < _k:
            _k = _k - l * (t - prev)
            prev = t
        else:
            heap.append([t, i])
            heap.sort(key=lambda x: x[1])
            heap = [[a-prev, b] for a, b in heap]
            break
    # print(heap)
    # print(f'_k = {_k}')

    curr = 0
    time = 0
    while time < _k:
        heap[curr][0] -= 1
        curr = (curr + 1) % len(heap)
        time = time + 1

    answer = heap[curr][1]
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