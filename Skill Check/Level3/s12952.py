# -*- coding: utf-8 -*-
"""
N-Queen : https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3
"""

answer = 0
def solution(n):
    global answer
    answer = 0

    def DFS(qList):
        global answer
        if len(qList) == n:
            # print(f'qList = {qList}')
            answer = answer + 1

        if len(qList) == 0:
            y = 0
        else:
            y = qList[-1][1] + 1

        for x in range(n):
            for _x, _y in qList:
                if _x == x:
                    break
                if _x + _y == x + y:
                    break
                if _x - _y == x - y:
                    break
            else:
                qList.append((x, y))
                DFS(qList)
                qList.remove((x, y))

    DFS([])

    return answer

if __name__ == '__main__':
    result = solution(4)
    print(f'result = {result}')
    assert result == 2

    result = solution(5)
    print(f'result = {result}')
    assert result == 10


