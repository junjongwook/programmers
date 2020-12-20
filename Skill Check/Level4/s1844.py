# -*- coding: utf-8 -*-
"""
게임 맵 최단거리 : https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
"""


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[float('inf')] * m for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = -1
    from collections import deque
    queue = deque()
    queue.append([[(0, 0)], 1])
    visited[0][0] = 1
    while queue:
        state = queue.popleft()
        # print(f'state = {state}')
        foot, distance = state
        y, x = foot[-1]
        if (y, x) == (n-1, m-1):
            answer = distance
            break
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            _distance = distance + 1
            if (_y, _x) in foot: continue
            if 0 <= _y < n and 0 <= _x < m and maps[_y][_x] == 1 and _distance < visited[_y][_x]:
                _foot = foot.copy()
                _foot.append((_y, _x))
                visited[_y][_x] = _distance
                queue.append([_foot, _distance])

    return answer


if __name__ == '__main__':
    result = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
    print(f'result = {result}')
    assert result == 11