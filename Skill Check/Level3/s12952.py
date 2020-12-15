# -*- coding: utf-8 -*-
"""
N-Queen : https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3
"""


def solution(n):
    answer = 0

    def next2(x, y):
        if x == y == -1:
            return (0, 0)
        _x = x + 1
        if _x < n:
            return (_x, y)
        _y = y + 1
        if _y < n:
            return (0, _y)

        return (-1, -1)

    from collections import deque
    queue = deque([])
    # 시작 포인트를 모두 queue 에 넣어 둔다.
    for y in range(n):
        for x in range(n):
            queue.append([(x, y)])

    while queue:
        qList = queue.popleft()
        if len(qList) == n:
            answer = answer + 1
            continue

        nX, nY = qList[-1]
        while True:
            nX, nY = next2(nX, nY)
            if nX == nY == -1:
                break
            for qX, qY in qList:
                if qX == nX or qY == nY:
                    break
                if qX + qY == nX + nY:
                    break
                if qX - qY == nX - nY:
                    break
            else:
                newQList = qList.copy()
                newQList.append((nX, nY))
                queue.append(newQList)

    return answer


if __name__ == '__main__':
    result = solution(4)
    print(f'result = {result}')
    assert result == 2

