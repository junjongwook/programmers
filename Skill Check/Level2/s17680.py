# -*- coding: utf-8 -*-
"""
[1차]캐시 : https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3#
"""


def solution(cacheSize, cities):
    from collections import deque
    cache = deque([])
    answer = 0
    for city in cities:
        _city = city.lower()
        if _city in cache:
            answer += 1
            cache.remove(_city)
            cache.append(_city)
        else:
            answer += 5
            cache.append(_city)
            if len(cache) > cacheSize:
                cache.popleft()

    return answer


if __name__ == '__main__':
    result = solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
    print(f'result = {result}')
    assert result == 50


