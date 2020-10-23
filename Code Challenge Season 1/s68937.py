# -*- coding: utf-8 -*-
'''
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
'''


def solution(n, edges):
    answer = 0
    from bisect import insort
    temp = []
    link = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        link[i][i] = 0
    for y, x in edges:
        link[y][x] = 1
        link[x][y] = 1
        insort(temp, 1)

    # Floyd-warshall
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            if s == m: continue
            for e in range(1, n + 1):
                if e == m: continue
                if s == e: continue
                if s > e: continue
                if link[s][e] == float('inf'):
                    _temp = link[s][m] + link[m][e]
                    if _temp != float('inf'):
                        link[s][e] = _temp
                        link[e][s] = _temp
                        insort(temp, _temp)
    answer = temp[-2]

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

