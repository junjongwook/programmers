# -*- coding: utf-8 -*-
'''
크레인 인형뽑기 게임 : https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
'''


def solution(board, moves):
    answer = 0
    stack = [0]
    for m in moves:
        index = m - 1
        pick = 0
        for i in range(len(board)):
            if board[i][index] == 0: continue
            pick = board[i][index]
            board[i][index] = 0
            if stack[-1] == pick:
                stack.pop()
                answer += 2
            else:
                stack.append(pick)
            break

    return answer


if __name__ == '__main__':
    result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    print(f'result = {result}')
    assert result == 4
