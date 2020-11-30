# -*- coding: utf-8 -*-
"""
다익스트라 : https://www.fun-coding.org/Chapter20-shortest-live.html
"""
import heapq


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    prev_node = {node: None for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        _distance, _node = heapq.heappop(queue)
        if distances[_node] < _distance:
            continue

        for adjacent, weight in graph[_node].items():
            distance = _distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                prev_node[adjacent] = _node

    print(prev_node)
    path = [end]
    while path[-1] != start:
        path.append(prev_node[path[-1]])
    path.reverse()
    return distances[end], path


if __name__ == '__main__':
    mygraph = {
        'A' : {'B': 8, 'C':1, 'D': 2},
        'B' : {},
        'C' : {'B' : 5, 'D' : 2},
        'D' : {'E' : 3, 'F' : 5},
        'E' : {'F' : 1},
        'F' : {'A' : 5}
    }
    result = dijkstra(mygraph, 'A', 'F')
    print(f'result = {result}')

