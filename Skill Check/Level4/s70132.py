# -*- coding: utf-8 -*-
"""
가짜 해밀토니안 : https://programmers.co.kr/learn/courses/30/lessons/70132
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)


def solution(t):
    adj = dict()
    for v1, v2 in t:
        adj.setdefault(v1, [])
        adj.setdefault(v2, [])
        adj[v1].append(v2)
        adj[v2].append(v1)
    # print(f'adj = {adj}')

    N = len(t)
    visited = [0] * (N + 1)
    queue = deque([(t[0][0], 0)])
    visited[t[0][0]] = 1
    while queue:
        v, d = queue.popleft()
        # print(f'v = {v}, d = {d}')
        for nv in adj[v]:
            if visited[nv] == 1: continue
            queue.append((nv, d+1))
            visited[nv] = 1

    start = v
    # print(f'start = {start}')
    queue = deque([(start,)])
    while queue:
        # print(f'queue = {queue}')
        diameter = queue.popleft()
        end = diameter[-1]
        for nv in adj[end]:
            if nv not in diameter:
                queue.append(diameter + (nv,))

    # print(f'diameter = {diameter}')

    def traverse(v, prev):
        # print(f'v = {v}, prev = {v}')
        temp = []
        for nxt in adj[v]:
            if nxt == prev: continue
            temp.append(traverse(nxt, v))

        if len(temp) == 0:
            return 1
        elif len(temp) == 1:
            return sum(temp) + 1

        temp.sort()
        if v in diameter:
            return sum(temp[-2:]) + 1
        else:
            return temp[-1] + 1

    answer = traverse(start, -1)

    return answer


if __name__ == '__main__':
    result = solution([[5, 1], [2, 5], [3, 5], [3, 6], [2, 4], [4, 0]])
    print(f'result = {result}')
    assert result == 7

    result = solution([[2, 5], [2, 0], [3, 2], [4, 2], [2, 1]])
    print(f'result = {result}')
    assert result == 4

    result = solution([[1, 0], [2, 8], [2, 7], [0, 2], [0, 3], [4, 0], [4, 5], [4, 6]])
    print(f'result = {result}')
    assert result == 8