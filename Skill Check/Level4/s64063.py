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
            answer.append(room)
            reserved[room] = room + 1
        else:
            other = reserved[room]
            while True:
                if other not in reserved:
                    answer.append(other)
                    reserved[room] = other + 1
                    reserved[other] = other + 1
                    break
                else:
                    other = reserved[other]

    return answer


if __name__ == '__main__':
    result = solution(10, [1, 3, 4, 1, 3, 1])
    print(f'result = {result}')
    assert result == [1, 3, 4, 2, 5, 6]


