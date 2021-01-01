# -*- coding: utf-8 -*-
"""
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
"""
from collections import deque

def solution(n, edges):
    d = dict()
    for v1, v2 in edges:
        d.setdefault(v1, [])
        d.setdefault(v2, [])
        d[v1].append(v2)
        d[v2].append(v1)
    # print(f'd= {d}')

    def distance(start):
        result = [float('inf')] * (n+1)
        result[0] = 0
        result[start] = 0
        queue = deque()
        for v in d[start]:
            queue.append((v, 1))
        while queue:
            v, d2 = queue.popleft()
            result[v] = d2
            for _v in d[v]:
                if result[_v] != float('inf'):
                    continue
                else:
                    queue.append((_v, d2 + 1))
        return result

    # 1번 에서 제일 먼 곳의 leaf node 를 찾기
    d3 = distance(1)
    # print(f'd3 = {d3}')
    leaf1 = d3.index(max(d3))
    print(f'leaf1 = {leaf1}')

    # leaf 에서 다른 leaf 을 찾기
    d4 = distance(leaf1)
    cnt = d4.count(max(d4))
    # leaf 이 두개이상 나온다면 그 값이 중간값으로 반환해도 된다.
    if cnt > 1:
        return max(d4)
    leaf2 = d4.index(max(d4))

    # 또다른 leaf 에서 leaf 이 있는지 확인
    d5 = distance(leaf2)
    cnt2 = d5.count(max(d5))
    # leaf 이 두개 이상 나온다면 그 값이 중간값으로 반환해도 된다.
    if cnt > 1:
        return max(d5)
    return max(d5) - 1


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    # result = solution(5, [[1,5],[2,5],[3,5],[4,5]])
    # print(f'result = {result}')
    # assert result == 2

