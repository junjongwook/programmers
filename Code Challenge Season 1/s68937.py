# -*- coding: utf-8 -*-
'''
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
'''


def solution(n, edges):
    answer = 0
    link = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    # 인자 정리
    for y, x in edges:
        link[y][x] = 1
        link[x][y] = 1
    # 같은 node 는 거리가 0
    for _n in range(n + 1):
        link[_n][_n] = 0

    # node 간의 최소 거리를 계산
    for y in range(1, n + 1):
        for x in range(y + 1, n + 1):
            if link[y][x] < float('inf'):
                for _x in range(1, n + 1):
                    if link[x][_x] < float('inf'):
                        link[y][_x] = min(link[y][x] + link[x][_x], link[y][_x])
                        link[_x][y] = link[y][_x]

    # 이제 번호 3개를 추출해서 거리의 중간을 가지고 배열을 만든다.
    temp = []
    from itertools import combinations
    for t in combinations(range(1, n + 1), 3):
        d1 = link[t[0]][t[1]]
        d2 = link[t[0]][t[2]]
        d3 = link[t[1]][t[2]]
        m = sorted([d1, d2, d3])[1]
        temp.append(m)

    answer = max(temp)
    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

