# -*- coding: utf-8 -*-
"""
블록 이동하기 : https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3
"""


def solution(board):
    answer = 0
    N = len(board)

    dxy = [
        [0, 1, 0],  # 우측으로 이동
        [1, 0, 0],  # 아래로 이동
        [0, -1, 0], # 좌측으로 이동
        [-1, 0, 0], # 위로 이동
        [1, 0, 1],  # 좌측(상측) 기준 시계방향 회전
        [1, 0, -1], # 좌측(상측) 기준 반시계 방향 회전
        [0, 1, 2],  # 우측(하측) 기준 시계방향 회전
        [0, 1, -2]  # 우측(상측) 기준 반시계 방향 회전
    ]

    def move(curr, delta):
        _curr = curr.copy()
        if delta[2] == 0:           # 단순 이동일 경우
            _curr[0] += delta[0]
            _curr[1] += delta[1]
        elif curr[2] == 0:          # 가로로 되어 있다면
            _curr[2] = 1
            if delta == [1, 0, 1]:      # 좌측기준 시계방향
                pass
            elif delta == [1, 0, -1]:   # 좌측 기준 반시계 방향
                _curr[0] = curr[0] - 1
            elif delta == [0, 1, 2]:    # 우측 시계방향
                _curr[0] = curr[0] - 1
                _curr[1] = curr[1] + 1
            elif delta == [0, 1, -2]:   # 우측 반시계 방향
                _curr[1] = curr[1] + 1
        elif curr[2] == 1:          # 세로로 되어 있다면
            _curr[2] = 0
            if delta == [1, 0, 1]:      # 상측기준 시계 방향
                _curr[1] = curr[1] - 1
            elif delta == [1, 0, -1]:   # 상측 기준 반시계 방향
                pass
            elif delta == [0, 1, 2]:    # 하측 시계 방향
                _curr[0] = curr[0] + 1
            elif delta == [0, 1, -2]:   # 하측 반시계 방향
                _curr[0] = curr[0] + 1
                _curr[1] = curr[1] - 1
                
        return _curr

    def isWall(curr):
        h, w, d = curr
        if d == 0:
            _h = h
            _w = w + 1
        else:
            _h = h + 1
            _w = w

        if h < 0 or w < 0 or _h < 0 or _w < 0:
            return True
        if h >= N or w >= N or _h >= N or _w >= N:
            return True
        if board[h][w]  == 1 or board[_h][_w] == 1:
            return True

        return False

    def isGoal(curr):
        h, w, d = curr
        if d == 0:
            _h = h
            _w = w + 1
        else:
            _h = h + 1
            _w = w

        if (h == w == N-1) or (_h == _w == N-1):
            return True

        return False

    from collections import deque
    queue = deque([([0, 0, 0], 0)])
    visited = [[0, 0, 0]]
    while queue:
        dron, n = queue.popleft()
        for _dxy in dxy:
            _dron = move(dron, _dxy)
            if isWall(_dron):
                continue
            if _dron in visited:
                continue
            if isGoal(_dron):
                return n + 1
            queue.append((_dron, n+1))
            visited.append(_dron)

    return -1


if __name__ == '__main__':
    result = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	)
    print(f'reulst = {result}')
    assert result == 7

#     result = solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
# )
#     print(f'result = {result}')
#     assert result == 21

    # result = solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]])
    # print(f'result = {result}')
    # assert result == 11

    # result = solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])
    # print(f'result = {result}')
    # assert result == 33
