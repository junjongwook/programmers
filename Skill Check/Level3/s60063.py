# -*- coding: utf-8 -*-
"""
블록 이동하기 : https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3
"""


def solution(board):
    answer = 0
    N = len(board)
    from collections import deque
    queue = deque([])
    queue.append([[(0, 0), (1, 0)]])

    def canGo(x, y):
        if 0 <= x < N and 0 <= y < N and board[y][x] == 0:
            return True
        else:
            return False

    def move(dron, direction):
        '''
            direction
            0 : 오른쪽 이동
            1 : 아래로 이동
            2 : 왼쪽 이동
            3 : 위로 이동
            4 : 왼쪽 혹은 위쪽 기준 시계 방향 회전
            5 : 왼쪽 혹은 위쪽 기준 반시계 방향 회전
            6 : 오른쪽 혹은 아래쪽 기준 시계 방향 회전
            7 : 오른쪽 혹은 아래쪽 기준 반시계 방향 회전
        '''
        (x1, y1), (x2, y2) = dron
        garo = y1 == y2     # 가로로 되어 있으면 True, 세로로 되어 있으면 False
        if garo:
            if direction == 0:
                if canGo(x2 + 1, y2):
                    return [(x2, y2), (x2 + 1, y2)]
            elif direction == 1:
                if canGo(x1, y1 + 1) and canGo(x2, y2 + 1):
                    return [(x1, y1 + 1), (x2, y2 + 1)]
            elif direction == 2:
                if canGo(x1 - 1, y1):
                    return [(x1 - 1, y1), (x1, y1)]
            elif direction == 3:
                if canGo(x1, y1 - 1) and canGo(x2, y2 - 1):
                    return [(x1, y1 -1), (x2, y2 - 1)]
            elif direction == 4:
                if canGo(x1, y1 + 1) and canGo(x2, y2 + 1):
                    return [(x1, y1), (x1, y1 + 1)]
            elif direction == 5:
                if canGo(x1, y1 - 1) and canGo(x2, y2 - 1):
                    return [(x1, y1 - 1), (x1, y1)]
            elif direction == 6:
                if canGo(x1, y1 -1) and canGo(x2, y2 - 1):
                    return [(x2, y2 - 1), (x2, y2)]
            elif direction == 7:
                if canGo(x1, y1 + 1) and canGo(x2, y2 + 1):
                    return [(x2, y2), (x2, y2 + 1)]
        else:
            if direction == 0:
                if canGo(x1 + 1, y1) and canGo(x2 + 1, y2):
                    return [(x1 + 1, y1), (x2 + 1, y2)]
            elif direction == 1:
                if canGo(x2, y2 + 1):
                    return [(x2, y2), (x2, y2 + 1)]
            elif direction == 2:
                if canGo(x1 - 1, y1) and canGo(x2 - 1, y2):
                    return [(x1 -1, y1), (x2 - 1, y2)]
            elif direction == 3:
                if canGo(x1, y1 - 1):
                    return [(x1, y1 - 1), (x1, y1)]
            elif direction == 4:
                if canGo(x1 - 1, y1) and canGo(x2, y2 - 1):
                    return [(x1 - 1, y1), (x1, y1)]
            elif direction == 5:
                if canGo(x1 + 1, y1) and canGo(x2 + 1, y2):
                    return [(x1, y1), (x1 + 1, y1)]
            elif direction == 6:
                if canGo(x1 + 1, y1) and canGo(x2 + 1, y2):
                    return [(x2, y2), (x2 + 1, y2)]
            elif direction == 7:
                if canGo(x1 - 1, y1) and canGo(x2 - 1, y2):
                    return [(x2 - 1, y2), (x2, y2)]

        return None

    while queue:
        dronFoot = queue.popleft()
        # print(f'dronFoot = {dronFoot}')
        last = dronFoot[-1]
        wing1, wing2 = last
        if wing1 == (N - 1, N - 1) or wing2 == (N - 1, N - 1):
            return len(dronFoot) - 1

        for i in range(8):
            _next = move(last, i)
            if _next is not None and _next not in dronFoot:
                _dronFoot = dronFoot.copy()
                _dronFoot.append(_next)
                queue.append(_dronFoot)

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
