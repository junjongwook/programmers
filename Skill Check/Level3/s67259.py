# -*- coding: utf-8 -*-
"""
경주로건설 : https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""
answer = float('inf')


def solution(board):
    global answer
    answer = float('inf')
    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    N = len(board)
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    def DFS(h, w, d, total):
        global answer
        # print(f'[({h}, {w}), {d}, {total}] -> ', end=' ')
        if h == w == N - 1:
            answer = min(answer, total)
            # print(f'answer = {answer}')
            return

        for _d in range(4):
            _h = h + dh[_d]
            _w = w + dw[_d]
            if 0 <= _h < N and 0 <= _w < N and board[_h][_w] == 0 and visited[_h][_w] == 0:
                _total = total + 100
                if _d != d:
                    _total += 500
                if _total > answer:
                    continue
                visited[_h][_w] = 1
                DFS(_h, _w, _d, _total)
                visited[_h][_w] = 0

    if board[0][1] == 0:
        DFS(0, 1, 0, 100)
    if board[1][0] == 0:
        DFS(1, 0, 1, 100)

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