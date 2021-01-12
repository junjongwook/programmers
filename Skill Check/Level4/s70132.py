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

    def traverse(v, prev):
        # print(f'v = {v}, prev = {v}')
        temp = []
        for nxt in adj[v]:
            if nxt == prev: continue
            temp.append(traverse(nxt, v))

        if len(temp) == 0:
            return 1
        elif len(temp) < 3:
            return sum(temp) + 1

        temp.sort()
        return sum(temp[-2:]) + 1

    answer = traverse(start, -1)

    return answer


if __name__ == '__main__':
    result = solution([[5, 1], [2, 5], [3, 5], [3, 6], [2, 4], [4, 0]])
    print(f'result = {result}')
    assert result == 7

    result = solution([[2, 5], [2, 0], [3, 2], [4, 2], [2, 1]])
    print(f'result = {result}')
    assert result == 4