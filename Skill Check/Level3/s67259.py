# -*- coding: utf-8 -*-
"""
경주로건설 : https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""
from collections import deque


def solution(board):
    answer = float('inf')

    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    N = len(board)

    queue = deque([])
    queue.append([[(0, 0)], -1, 0])     # 현재 위치, 이전 방향, 현재까지 비용

    while queue:
        paths, direction, total = queue.popleft()
        if paths[-1] == (N - 1, N - 1):
            answer = min(answer, total)
            # print(f'paths = {paths}, direction = {direction}, total = {total}')
            continue
        h, w = paths[-1]
        for d in range(4):
            _h = h + dh[d]
            _w = w + dw[d]
            if (_h, _w) in paths:
                continue
            if 0 <= _h < N and 0 <= _w < N and board[_h][_w] == 0:
                _total = total + 100
                if direction != -1 and d != direction:
                    _total += 500
                if _total > answer:
                    continue
                queue.append([paths + [(_h, _w)], d, _total])

    return answer


if __name__ == '__main__':
    result = solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(f'result = {result}')
    assert result == 900

    result = solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
    print(f'result = {result}')
    assert result == 2100

    result = solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
    print(f'result = {result}')
    assert result == 3800