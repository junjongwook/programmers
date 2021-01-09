# -*- coding: utf-8 -*-
"""
호텔 방 배정 : https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3
"""


def solution(k, room_number):
    answer = []
    N = len(room_number)
    reserved = set()
    for i in range(N):
        num = room_number[i]
        if num not in reserved:
            reserved.add(num)
            answer.append(num)
        else:
            for j in range(num + 1, k + 1):
                if j not in reserved:
                    reserved.add(j)
                    answer.append(j)
                    break
    return answer


if __name__ == '__main__':
    result = solution(10, [1, 3, 4, 1, 3, 1])
    print(f'result = {result}')
    assert result == [1, 3, 4, 2, 5, 6]


