# -*- coding: utf-8 -*-
"""
배달 : https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3
"""


def solution(N, road, K):
    answer = 0
    result = set()
    graph = dict()
    for v1, v2, d in road:
        graph.setdefault(v1, dict())
        graph.setdefault(v2, dict())
        if v1 in graph and v2 in graph[v1]:
            graph[v1][v2] = min(graph[v1][v2], d)
            graph[v2][v1] = min(graph[v2][v1], d)
        else:
            graph[v1][v2] = d
            graph[v2][v1] = d
    distances = [float('inf')] * (N + 1)
    distances[1] = 0
    result.add(1)
    import heapq
    queue = []
    heapq.heappush(queue, (distances[1], 1))

    while queue:
        _distance, _node = heapq.heappop(queue)
        if distances[_node] < _distance:
            continue

        for adjacent, weight in graph[_node].items():
            distance = distances[_node] + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                if distance <= K:
                    result.add(adjacent)
                heapq.heappush(queue, (distance, adjacent))

    answer = len(result)

    return answer


if __name__ == '__main__':
    result = solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
    print(f'result = {result}')
    assert result == 4


