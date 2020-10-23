# -*- coding: utf-8 -*-
'''
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
'''


def solution(n, edges):
    answer = 0
    link = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        link[i][i] = 0
    for y, x in edges:
        link[y][x] = 1
        link[x][y] = 1

    # Floyd-warshall
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            if s == m: continue
            for e in range(1, n + 1):
                if e == m: continue
                if s == e: continue
                link[s][e] = min(link[s][m] + link[m][e], link[s][e])
                link[e][s] = link[s][e]

    # 이제 번호 3개를 추출해서 거리의 중간을 가지고 배열을 만든다.
    from itertools import combinations
    answer = 0
    for t in combinations(range(1, n + 1), 3):
        d1 = link[t[0]][t[1]]
        d2 = link[t[0]][t[2]]
        d3 = link[t[1]][t[2]]
        if sorted([d1, d2, d3])[1] > answer:
            answer = sorted([d1, d2, d3])[1]

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

