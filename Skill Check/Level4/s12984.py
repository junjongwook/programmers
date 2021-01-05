# -*- coding: utf-8 -*-
"""
지형 편집 : https://programmers.co.kr/learn/courses/30/lessons/12984?language=python3
"""


def solution(land, P, Q):
    answer = float('inf')
    block = dict()
    N = len(land)
    # 블록높이 : 좌표개수 의 dictionary 정보를 만든다.
    for i in range(N):
        for j in range(N):
            height = land[i][j]
            block.setdefault(height, 0)
            block[height] += 1
    # print(block)

    _N = len(block) + 1     # 맨 앞의 dummy 용을 넣어서 계산할 때 편하게 하자

    m = [
        [0] * _N,   # 0 : 블록높이
        [0] * _N,   # 1 : 좌표개수
        [0] * _N,   # 2 : 좌표개수 prefix sum
        [0] * _N,   # 3 : 블록개수 = 블록높이 * 좌표개수
        [0] * _N,   # 4 : 블록개수 prefix sum
    ]

    # dictionary 로 되어 있는 블록높이 : 좌표개수 정보를 정렬해서 반영한다.
    keys = sorted(block.keys())
    # print(f'keys = {keys}')
    for i in range(1, _N):
        m[0][i] = keys[i-1]
        m[1][i] = block[m[0][i]]
        m[2][i] = m[2][i-1] + m[1][i]
        m[3][i] = m[0][i] * m[1][i]
        m[4][i] = m[4][i-1] + m[3][i]

    # print(*m, sep='\n')

    # 기준점을 잡아서 좌측은 블록을 추가, 우측은 블록을 제거하는 식으로 계산
    for i in range(1, _N):
        # 기준점의 블록높이로 평탄화 작업 높이로 한다.
        height = m[0][i]
        
        # 좌측 좌표 개수, 블록 총 개수
        leftCoord = m[2][i]
        leftBlocks = m[4][i]
        # 필요한 block 의 수, 메꾸는데 드는 총 비용
        leftExpectedBlocks = leftCoord * height
        totalP = (leftExpectedBlocks - leftBlocks) * P

        # 우측 좌표 개수, 블록 총 개수
        rightCoord = m[2][-1] - m[2][i]
        rightBlocks = m[4][-1] - m[4][i]
        # 필요한 block 의 수, 치우는데 드는 총 비용
        rightExpectedBlocks = rightCoord * height
        totalQ = (rightBlocks - rightExpectedBlocks) * Q

        # print(f'i = {i}, height = {height}, totalP = {totalP}, totalQ = {totalQ}, totalP + totalQ = {totalP + totalQ}')
        if answer > (totalP + totalQ):
            answer = totalP + totalQ

    return answer


if __name__ == '__main__':
    result = solution([[1, 2], [2, 3]], 3, 2)
    print(f'result = {result}')
    assert result == 5

    # result = solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3)
    # print(f'result = {result}')
    # assert result == 33
