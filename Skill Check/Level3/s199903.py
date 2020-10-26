# -*- coding: utf-8 -*-
'''

'''

def solution(n, edge):
    answer = 0
    edgeDict = dict()
    for v1, v2 in edge:
        edgeDict.setdefault(v1, [])
        edgeDict.setdefault(v2, [])
        edgeDict[v1].append(v2)
        edgeDict[v2].append(v1)

    distance = [float('inf')] * (n + 1)
    visited = [0] * (n + 1)
    distance[1] = 0

    from collections import deque
    queue = deque([1])
    while queue:
        _n = queue.popleft()
        visited[_n] = 1
        for _next in edgeDict[_n]:
            distance[_next] = min(distance[_next], distance[_n] + 1)
            if visited[_next] == 0:
                queue.append(_next)

    _max = max(list(filter(lambda n : n != float('inf'), distance)))
    answer = distance.count(_max)
    return answer


if __name__ == '__main__':
    result = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    print(f'result={result}')
    assert result == 3
