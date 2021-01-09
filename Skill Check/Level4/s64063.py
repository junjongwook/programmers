# -*- coding: utf-8 -*-
"""
호텔 방 배정 : https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3
"""


def solution(k, room_number):
    answer = []
    N = len(room_number)
    reserved = dict()
    for room in room_number:
        if room not in reserved:
            reserved[room] = room + 1
            answer.append(room)
        else:
            for other in range(reserved[room], k+1):
                if other not in reserved:
                    reserved[other] = other + 1
                    reserved[room] = other + 1
                    answer.append(other)
                    break

    return answer


if __name__ == '__main__':
    result = solution(10, [1, 3, 4, 1, 3, 1])
    print(f'result = {result}')
    assert result == [1, 3, 4, 2, 5, 6]


