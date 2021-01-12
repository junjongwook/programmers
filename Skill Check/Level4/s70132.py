# -*- coding: utf-8 -*-
"""
가짜 해밀토니안 : https://programmers.co.kr/learn/courses/30/lessons/70132
"""
import sys
sys.setrecursionlimit(10**6)
adj = dict()
drr = [0] * 200_003
ans = 0

def dfs(node, dep, pre):
    # print(f'node = {node}, dep = {dep}, pre = {pre}')
    drr[node] = dep
    for there in adj[node]:
        if there == pre: continue
        dfs(there, dep + 1, node)


def fun(node, pre):
    global ans
    a = []
    b = []
    for there in adj[node]:
        if there == pre: continue
        tem = fun(there, node)
        a.append((tem[0], there))
        b.append((tem[1], there))

    if len(a) == 0:
        ans = max(ans, 1 + drr[node])
        return (1, 1)
    elif len(a) == 1:
        ans = max(ans, b[0][0] + 1 + drr[node])
        return (a[0][0] + 1, b[0][0] + 1)
    a.sort()
    b.sort()
    n = len(a)
    if a[n-1][1] != b[n-1][1]:
        ans = max(ans, b[n - 1][0] + b[n - 2][0] + 1 + drr[node])
        return (a[n - 1][0] + 1, b[n - 1][0] + a[n - 1][0] + 1)
    else:
        ans = max(ans, b[n - 1][0] + b[n - 2][0] + 1 + drr[node])
        return (a[n - 1][0] + 1, max(b[n - 1][0] + a[n - 2][0] + 1, b[n - 2][0] + a[n - 1][0] + 1))


def solution(t):
    global adj, drr, ans
    adj = dict()
    drr = [0] * 200_003
    ans = 0
    answer = 0
    n = len(t) + 1
    for v1, v2 in t:
        adj.setdefault(v1, [])
        adj.setdefault(v2, [])
        adj[v1].append(v2)
        adj[v2].append(v1)
    # print(f'adj = {adj}')

    dfs(1, 0, -1)
    temnode = 1
    temdep = 0
    for i in range(n):
        if temdep < drr[i]:
            temnode = i
            temdep = drr[i]

    dfs(temnode, 0, -1)
    temdep = 0
    for i in range(n):
        if temdep < drr[i]:
            temnode = i
            temdep = drr[i]

    dfs(temnode, 0, -1)
    fun(temnode, -1)
    answer = ans

    return answer


if __name__ == '__main__':
    result = solution([[5, 1], [2, 5], [3, 5], [3, 6], [2, 4], [4, 0]])
    print(f'result = {result}')
    assert result == 7

    result = solution([[2, 5], [2, 0], [3, 2], [4, 2], [2, 1]])
    print(f'result = {result}')
    assert result == 4