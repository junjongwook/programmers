# -*- coding: utf-8 -*-
"""
스티커모으기(2) : https://programmers.co.kr/learn/courses/30/lessons/12971?language=python3
"""


def solution(sticker):
    N = len(sticker)
    if N <= 3: return max(sticker)
    if N == 4: return max(sticker[0] + sticker[2], sticker[1] + sticker[3])

    # 0번째 부터 시작할 경우는 맨 끝은 갈 수 없다
    temp = [0] * (N - 1)
    answer = 0
    temp[0] = sticker[0]
    temp[2] = temp[0] + sticker[2]
    for i in range(3, N - 1):
        temp[i] = max(sticker[i] + temp[i-2], sticker[i] + temp[i-3])
        if temp[i] > answer: answer = temp[i]

    # 1번째부터 시작할 경우는 맨 끝까지 갈 수 있다.
    temp = [0] * N
    temp[0] = 0
    temp[1] = sticker[1]
    temp[2] = 0
    for i in range(3, N):
        temp[i] = max(sticker[i] + temp[i-2], sticker[i] + temp[i-3])
        if temp[i] > answer: answer = temp[i]

    return answer


if __name__ == '__main__':
    result = solution([14, 6, 5, 11, 3, 9, 2, 10])
    print(f'result = {result}')
    assert result == 36

    result = solution([1, 3, 2, 5, 4])
    print(f'result = {result}')
    assert result == 8