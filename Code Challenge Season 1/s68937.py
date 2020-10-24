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
    start = edges[0][0]
    from collections import deque
    queue = deque([[start]])
    end = start
    while queue:
        vertices = queue.popleft()
        end = vertices[-1]
        for next in edgeDict[end]:
            if next not in vertices:
                _temp = vertices.copy()
                _temp.append(next)
                queue.append(_temp)

    # 찾은 노드에서 다시 제일 먼 노드를 찾는다. 이 때 거리가 트리의 지름이 된다.
    start = end
    queue = deque([[start]])
    maxDistance = 0
    end = start
    while queue:
        vertices = queue.popleft()
        _distance = len(vertices) - 1
        if maxDistance < _distance:
            maxDistance = _distance
            check = False   # 새로 등장한 거리라면 값이 중복되지 않는다.
        else:
            check = True    # 이전 값과 동일하므로 값이 중복된다. 나중에 보면 트리 지름이 2개 이상이 된다.
        end = vertices[-1]
        for next in edgeDict[end]:
            if next not in vertices:
                _temp = vertices.copy()
                _temp.append(next)
                queue.append(_temp)

    if check:   # 트리 지름이 2개 이상 있을 경우
        answer = maxDistance
    else:
        answer = maxDistance - 1

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

