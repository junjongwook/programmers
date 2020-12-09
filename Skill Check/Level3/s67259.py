# -*- coding: utf-8 -*-
"""
경주로건설 : https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""
import sys
answer = float('inf')
index = 0

def solution(board):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    N = len(board)

    visited = [[0] * N for _ in range(N)]

    def canGo(h, w):
        if h < 0 or w < 0: return False
        if h >= N or w >= N: return False
        if board[h][w] == 1: return False
        if visited[h][w] == 1: return False

        return True

    def DFS(curr, d, total):
        global index
        print(f'curr = {curr}, d = {d}, total = {total}')
        index = index + 1
        if index > 1000: sys.exit(0)

        global answer
        _h = curr[0] + dxy[d][0]
        _w = curr[1] + dxy[d][1]
        if not canGo(_h, _w):
            return

        if _h == N - 1 and _w == N - 1:
            answer = min(answer, total)
            return

        visited[_h][_w] = 1
        for _d in range(4):
            if _d == d: DFS((_h, _w), _d, total + 100)
            else:
                DFS((_h, _w), _d, total + 100 + 500)
        visited[_h][_w] = 0

        return

    visited[0][0] = 1
    DFS([0, 0], 0, 100)
    DFS([0, 0], 1, 100)
    DFS([0, 0], 2, 100)
    DFS([0, 0], 3, 100)
    visited[0][0] = 0

    return answer


if __name__ == '__main__':
    # result = solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # print(f'result = {result}')
    # assert result == 900

    # result = solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
    # print(f'result = {result}')
    # assert result == 2100

    result = solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
    print(f'result = {result}')
    assert result == 3800