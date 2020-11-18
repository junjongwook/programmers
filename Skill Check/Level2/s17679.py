# -*- coding: utf-8 -*-
"""
[1차]프렌즈4블록 : https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3
"""


def solution(m, n, board):
    answer = 0
    nBoard = [list(_b) for _b in board]

    while True:
        # 삭제할 대상을 찾기
        toDelete = set()
        for h in range(1, m):
            for w in range(1, n):
                if nBoard[h][w] == ' ': continue
                if nBoard[h][w] == nBoard[h-1][w] == nBoard[h][w-1] == nBoard[h-1][w-1]:
                    toDelete.add((h, w))
                    toDelete.add((h-1, w))
                    toDelete.add((h, w-1))
                    toDelete.add((h-1, w-1))
        # 삭제할게 없으면 끝냄
        if len(toDelete) == 0: break

        answer = answer + len(toDelete)

        # 삭제하기
        for _h, _w in list(toDelete):
            nBoard[_h][_w] = ' '

        # 빈공간 채우기
        while True:
            exitFlag = True
            for _h in range(m-1, 0, -1):
                for _w in range(n):
                    if nBoard[_h][_w] == ' ':
                        nBoard[_h][_w] = nBoard[_h-1][_w]
                        nBoard[_h-1][_w] = ' '
                        if nBoard[_h][_w] != ' ':
                            exitFlag = False
            if exitFlag:
                break

    return answer


if __name__ == '__main__':
    result = solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
    print(f'result = {result}')
    assert result == 15

