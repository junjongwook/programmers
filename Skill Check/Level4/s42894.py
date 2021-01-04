# -*- coding: utf-8 -*-
"""
블록 게임 : https://programmers.co.kr/learn/courses/30/lessons/42894?language=python3
"""


def solution(board):
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
        if equal(num, h, w + 1):                # 오른쪽(+1) 확인
            if equal(num, h, w + 2):            # 오른쪽(+2) 확인
                if equal(num, h + 1, w + 2):    # 오른쪽(+2), 아래쪽(+1) 확인
                    return 1, False                             # 1번 type 이면서 제거 불가능
                elif equal(num, h + 1, w):      # 오른쪽(0), 아래쪽(+1) 확인
                    return 5, False                             # 5번 type 이면서 제거 불가능
                elif equal(num, h + 1, 2 + 1):  # 오른쪽(+1), 아래쪽(+1) 확인
                    return 11, False                            # 11번 type, 제거 불가능
            elif equal(num, h + 1, w) and equal(num, h + 2, w):
                return 2, False                                 # 2번 type, 제거 불가능
            elif equal(num, h + 1, w + 1) and equal(num, h + 2, w + 1):
                return 8, False                                 # 8번 type, 제거 불가능
        elif equal(num, h + 1, w) and equal(num, h + 2, w): # 아래로 3개 연달아 있는 블록들
            if equal(num, h + 2, w - 1):
                return 4, True                                  # 4번 type, 제거 가능
            elif equal(num, h + 2, w + 1):
                return 6, True                                  # 6번 type, 제거 가능
            elif equal(num, h + 1, w + 1):
                return 10, False                                # 10번 type, 제거 불가능
            elif equal(num, h + 1, w - 1):
                return 12, False                                # 12번 type, 제거 불가능
        elif equal(num, h + 1, w):
            if equal(num, h +1, w + 1) and equal(num, h + 1, w + 2):
                return 3, True                                  # 3번 type, 제거 가능
            elif equal(num, h + 1, w - 1) and equal(num, h + 1, w - 2):
                return 7, True                                  # 7번 type, 제거 가능
            elif equal(num, h + 1, w - 1) and equal(num, h + 1, w + 1):
                return 9, True                                  # 9번 type, 제거 가능

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

    for h in range(height):
        for w in range(width):
            if board[h][w] <= 0: continue
            type, erasable = kindBlock(h, w)
            if erasable and erase(type, h, w):
                answer += 1
            else:
                visited(type, h, w)

    return answer


if __name__ == '__main__':
    result = solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])
    print(f'result = {result}')
    assert result == 2