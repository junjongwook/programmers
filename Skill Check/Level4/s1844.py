# -*- coding: utf-8 -*-
"""
게임 맵 최단거리 : https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
"""


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = -1
    from collections import deque
    queue = deque()
    queue.append([(0, 0)])
    while queue:
        foot = queue.popleft()
        # print(f'foot = {foot}')
        if foot[-1] == (n-1, m-1):
            answer = len(foot)
            break
        y, x = foot[-1]
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if (_y, _x) in foot: continue
            if 0 <= _y < n and 0 <= _x < m and maps[_y][_x] == 1:
                _foot = foot.copy()
                _foot.append((_y, _x))
                queue.append(_foot)

    return answer


if __name__ == '__main__':
    result = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
    print(f'result = {result}')
    assert result == 11