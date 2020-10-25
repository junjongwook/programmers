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

    from collections import deque

    def 거리구하기(start) -> []:
        visited = [0] * (n + 1)
        distance = [0] * (n + 1)
        queue = deque([])
        queue.append(start)
        visited[start] = 1
        while queue:
            vertex = queue.popleft()
            nextVertex = edgeDict[vertex]
            for _next in nextVertex:
                if visited[_next] == 1: continue
                distance[_next] = distance[vertex] + 1
                visited[_next] = 1
                queue.append(_next)

        return distance

    result = 거리구하기(edges[0][0])
    _max = max(result)  # 최대 거리 구하기
    _startList = []     # 최대 거리 위치 목록
    _startIndex = 0
    try:
        index = result.index(_max, _startIndex)
        _startList.append(index)
    except ValueError:
        pass

    for _start in _startList:
        result = 거리구하기(_start)
        _max = max(result)
        _count = result.count(_max)
        if _count > 1:
            answer = _max
            break
        answer = max(answer, _max - 1)

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

