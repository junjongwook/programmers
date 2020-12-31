# -*- coding: utf-8 -*-
"""
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
"""


def solution(n, edges):
    answer = 0
    m = [[float('inf')] * (n+1) for _ in range(n+1)]
    for h, v in edges:
        m[h][v] = 1
        m[v][h] = 1
    for i in range(n+1):
        m[0][i] = 0
        m[i][i] = 0
        m[i][0] = 0

    for h in range(1, n):
        for v in range(h + 1, n + 1):
            for k in range(1, n + 1):
                if k == h or k == v: continue
                m[h][v] = min(m[h][v], m[h][k] + m[k][v])
                m[v][h] = m[h][v]

    # print(*m, sep='\n')

    _max = 0
    for h in range(1, n):
        for v in range(h + 1, n + 1):
            for k in range(1, n + 1):
                if k == h or k == v: continue
                _sum = sum([m[h][v], m[h][k], m[k][v]])
                if _sum > _max:
                    _max = _sum

    answer = _max // 3

    return answer


if __name__ == '__main__':
    # result = solution(4, [[1,2],[2,3],[3,4]])
    # print(f'result = {result}')
    # assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]])
    print(f'result = {result}')
    assert result == 2

