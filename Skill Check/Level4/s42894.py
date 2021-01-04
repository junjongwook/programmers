# -*- coding: utf-8 -*-
"""
블록 게임 : https://programmers.co.kr/learn/courses/30/lessons/42894?language=python3
"""


def solution(board):
    # print(*board, sep='\n')
    answer = 0
    height = len(board)
    width = len(board[0])

    def equal(n, h, w):
        if h < 0 or w < 0 or h >= height or w >= width:
            return False
        if board[h][w] == n:
            return True
        return False
    
    def kindBlock(h, w):
        '''
        시작 포인트를 기준으로 블락의 종류를 판단한다. 회전한 형태를 각각의 하나의 경우로 생각한다.
        '''
        num = board[h][w]
        if equal(num, h, w + 1) and equal(num, h, w + 2) and equal(num, h + 1, w + 2):
            return 1, False
        elif equal(num, h, w + 1) and equal(num, h + 1, w) and equal(num, h + 2, w):
            return 2, False
        elif equal(num, h + 1, w) and equal(num, h + 1, w + 1) and equal(num, h + 1, w + 2):
            return 3, True
        elif equal(num, h + 1, w) and equal(num, h + 2, w) and equal(num, h + 2, w - 1):
            return 4, True
        elif equal(num, h, w + 1) and equal(num, h, w + 2) and equal(num, h + 1, w):
            return 5, False
        elif equal(num, h + 1, w) and equal(num, h + 2, w) and equal(num, h + 2, w + 1):
            return 6, True
        elif equal(num, h + 1, w) and equal(num, h + 1, w - 1) and equal(num, h + 1, w - 2):
            return 7, True
        elif equal(num, h, w + 1) and equal(num, h + 1, w + 1) and equal(num, h + 2, w + 1):
            return 8, False
        elif equal(num, h + 1, w - 1) and equal(num, h + 1, w) and equal(num, h + 1, w + 1):
            return 9, True
        elif equal(num, h + 1, w) and equal(num, h + 1, w + 1) and equal(num, h + 2, w):
            return 10, False
        elif equal(num, h, w + 1) and equal(num, h, w + 2) and equal(num, h + 1, w + 1):
            return 11, False
        elif equal(num, h + 1, w) and equal(num, h + 1, w - 1) and equal(num, h + 2, w):
            return 12, False

        return None, False

    def erase(type, h, w): 
        '''
        삭제 가능하다면 삭제하고, True 반환 그렇지 않다면 False 반환
        '''
        if type == 3:
            for _h in range(h + 1):
                if board[_h][w+1] != 0 or board[_h][w+2] != 0:
                    return False
            board[h][w] = 0
            board[h+1][w] = 0
            board[h+1][w+1] = 0
            board[h+1][w+2] = 0
            return True
        elif type == 4:
            for _h in range(h + 2):
                if board[_h][w - 1] != 0:
                    return False
            board[h][w] = 0
            board[h+1][w] = 0
            board[h+2][w] = 0
            board[h+2][w-1] = 0
            return True
        elif type == 6:
            for _h in range(h + 2):
                if board[_h][w + 1] != 0:
                    return False
            board[h][w] = 0
            board[h+1][w] = 0
            board[h+2][w] = 0
            board[h+2][w+1] = 0
            return True
        elif type == 7:
            for _h in range(h + 1):
                if board[_h][w - 2] != 0 or board[_h][w - 1] != 0:
                    return False
            board[h][w] = 0
            board[h+1][w] = 0
            board[h+1][w-1] = 0
            board[h+1][w-2] = 0
            return True
        elif type == 9:
            for _h in range(h + 1):
                if board[_h][w - 1] != 0 or board[_h][w + 1] != 0:
                    return False
            board[h][w] = 0
            board[h+1][w] = 0
            board[h+1][w-1] = 0
            board[h+1][w+1] = 0
            return True

        return False

    def visited(type, h, w):
        '''
        삭제가 불가능하면 방문한 것으로 처리한다. 0 으로 할 수 없으니 -1 로 처리한다.
        '''
        if type == 1:
            board[h][w] = -1
            board[h][w+1] = -1
            board[h][w+2] = -1
            board[h+1][w+2] = -1
        elif type == 2:
            board[h][w] = -1
            board[h][w+1] = -1
            board[h+1][w] = -1
            board[h+2][w] = -1
        elif type == 3:
            board[h][w] = -1
            board[h+1][w] = -1
            board[h+1][w+1] = -1
            board[h+1][w+2] = -1
        elif type == 4:
            board[h][w] = -1
            board[h+1][w] = -1
            board[h+2][w] = -1
            board[h+2][w-1] = -1
        elif type == 5:
            board[h][w] = -1
            board[h][w+1] = -1
            board[h][w+2] = -1
            board[h+1][w] = -1
        elif type == 6:
            board[h][w] = -1
            board[h+1][w] = -1
            board[h+2][w] = -1
            board[h+2][w+1] = -1
        elif type == 7:
            board[h][w] = -1
            board[h+1][w] = -1
            board[h+1][w-1] = -1
            board[h+1][w-2] = -1
        elif type == 8:
            board[h][w] = -1
            board[h][w+1] = -1
            board[h+1][w+1] = -1
            board[h+2][w+1] = -1
        elif type == 9:
            board[h][w] = -1
            board[h+1][w-1] = -1
            board[h+1][w] = -1
            board[h+1][w+1] = -1
        elif type == 10:
            board[h][w] = -1
            board[h+1][w] = -1
            board[h+1][w+1] = -1
            board[h+2][w] = -1
        elif type == 11:
            board[h][w] = -1
            board[h][w+1] = -1
            board[h][w+2] = -1
            board[h+1][w+1] = -1
        elif type == 12:
            board[h][w] = -1
            board[h+1][w-1] = -1
            board[h+1][w] = -1
            board[h+2][w] = -1

        return

    h, w = 0, 0
    while h < height:
        if board[h][w] > 0:
            type, erasable = kindBlock(h, w)
            if type != None and erasable and erase(type, h, w):
                answer += 1
                w = 0
                continue
        w = w + 1
        if w == width:
            h += 1
            w = 0

    return answer


if __name__ == '__main__':
    result = solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])
    print(f'result = {result}')
    assert result == 2

    result = solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
    print(f'result = {result}')
    assert result == 1

    result = solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
    print(f'result = {result}')
    assert result == 2
