# -*- coding: utf-8 -*-
"""
경주로건설 : https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""


def solution(board):
    global answer
    N = len(board)
    map = [[float('inf') for a in range(N)] for _ in range(N)]
    from collections import deque
    queue = deque()
    # 방향 전환 ==> 0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue.append((0, 0, 0, 100))
    queue.append((0, 0, 1, 100))
    map[0][0] = 0

    while queue:
        _x, _y, _d, _c = queue.popleft()
        # print('_x, _y, _d, _c =', _x, _y, _d, _c, end=' ')
        nx = _x + dx[_d]
        ny = _y + dy[_d]
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0 and _c <= map[ny][nx]:
            map[ny][nx] = _c
            # print('ok')
            for i in range(4):  # 4방향으로 가본다.
                if _d == i:
                    queue.append((nx, ny, i, _c + 100))
                else:
                    queue.append((nx, ny, i, _c + 600))
        # else:
        #     print()

    answer = map[N-1][N-1]

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