# -*- coding: utf-8 -*-
"""
지형 이동 : https://programmers.co.kr/learn/courses/30/lessons/62050?language=python3
"""


def solution(land, height):
    answer = 0
    N = len(land)
    visited = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    from collections import deque
    import heapq
    ladder = []
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    count = 0

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            _y = y + dy[d]
            _x = x + dx[d]
            if 0 <= _x < N and 0 <= _y < N:
                if visited[_y][_x] == 1: continue
                _height = abs(land[y][x] - land[_y][_x])
                if _height > height:
                    heapq.heappush(ladder, (_height, _y, _x))
                else:
                    queue.append((_y, _x))
                    visited[_y][_x] = 1

        if len(queue) == 0:

            while len(ladder) > 0:
                _height, _y, _x = heapq.heappop(ladder)
                if visited[_y][_x] == 1: continue
                answer = answer + _height
                queue.append((_y, _x))
                visited[_y][_x] = 1
                break

    return answer


if __name__ == '__main__':
    result = solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
    print(f'result = {result}')
    assert result == 15