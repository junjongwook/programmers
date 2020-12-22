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
    ladder = []
    queue = deque()
    queue.append((0, 0))
    count = 0

    while queue:
        y, x = queue.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            for d in range(4):
                _y = y + dy[d]
                _x = x + dx[d]
                if 0 <= _y < N and 0 <= _x < N:
                    if visited[_y][_x] == 1: continue
                    _height = abs(land[y][x] - land[_y][_x])
                    if _height > height:
                        ladder.append((_height, _y, _x))
                    else:
                        queue.append((_y, _x))

        if len(queue) == 0:
            ladder.sort(reverse=True)
            while len(ladder) > 0:
                _height, _y, _x = ladder.pop()
                if visited[_y][_x] == 1: continue
                answer = answer + _height
                queue.append((_y, _x))
                break

    return answer


if __name__ == '__main__':
    result = solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
    print(f'result = {result}')
    assert result == 15