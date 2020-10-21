# -*- coding: utf-8 -*-
'''
삼각 달팽이 : https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
'''


def solution(n):
    answer = []
    temp = [[0] * (_n + 1) for _n in range(n)]
    dxy = [(1, 0), (0, 1), (-1, -1)] # 아래로, 오른쪽으로, 좌상단으로
    curr_dxy = 0
    curr = [0, 0]

    length = sum([len(t) for t in temp])
    for i in range(1, length + 1):
        temp[curr[0]][curr[1]] = i

        temp_curr = [
            curr[0] + dxy[curr_dxy][0],
            curr[1] + dxy[curr_dxy][1]
        ]
        if temp_curr[0] < 0 or temp_curr[1] < 0 \
            or temp_curr[0] >= n \
            or temp_curr[1] >= len(temp[temp_curr[0]]) \
            or temp[temp_curr[0]][temp_curr[1]] != 0:
            curr_dxy = (curr_dxy + 1) % len(dxy)
            curr = [
                curr[0] + dxy[curr_dxy][0],
                curr[1] + dxy[curr_dxy][1]
            ]
        else:
            curr = temp_curr

    for t in temp:
        answer.extend(t)

    return answer


if __name__ == '__main__':
    result = solution(4)
    print(f'result = {result}')
    assert result == [1,2,9,3,10,8,4,5,6,7]

    result = solution(5)
    print(f'result = {result}')
    assert result == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

    result = solution(6)
    assert result == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]