# -*- coding: utf-8 -*-
'''
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
'''


def solution(n, edges):
    answer = 0
    edgeDict = dict()
    for v1, v2 in edges:
        edgeDict.setdefault(v1, [])
        edgeDict.setdefault(v2, [])
        edgeDict[v1].append(v2)
        edgeDict[v2].append(v1)

    # 첫번째 노드에서 제일 먼 곳의 노드를 하나 찾는다.
    visited = [0] * (n+1)
    stack = [(edges[0][0], 0)]
    lastVertex = edges[0][0]
    longDistance = 0
    while stack:
        vertex, distance = stack.pop()
        visited[vertex] = 1
        if distance > longDistance:
            lastVertex = vertex
            longDistance = distance
        for nextEdge in edgeDict[vertex]:
            if visited[nextEdge] == 0:
                stack.append((nextEdge, distance + 1))

    # 찾은 노드에서 다시 제일 먼 노드를 찾는다. 이 때 거리가 트리의 지름이 된다.
    import bisect
    temp = []
    visited = [0] * (n + 1)
    stack = [(lastVertex, 0)]
    longDistance = -1
    onlyLast = True
    while stack:
        vertex, distance = stack.pop()
        bisect.insort(temp, distance)
        visited[vertex] = 1
        if distance > longDistance:
            lastVertex = vertex
            longDistance = distance
            onlyLast = True
        else:
            onlyLast = False
        for nextEdge in edgeDict[vertex]:
            if visited[nextEdge] == 0:
                stack.append((nextEdge, distance + 1))

    # if onlyLast:   # 트리 지름이 1개만 존재할 경우
    #     answer = longDistance - 1
    # else:
    #     answer = longDistance

    if temp[-1] == temp[-2]:
        answer = longDistance
    else:
        answer = longDistance - 1

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

