# -*- coding: utf-8 -*-
"""
호텔 방 배정 : https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3
"""
from bisect import bisect_right, insort_right

def solution(k, room_number):
    answer = []
    N = len(room_number)
    reserved = []
    for i in range(N):
        num = room_number[i]
        rindex = bisect_right(reserved, num)
        if rindex == 0 or reserved[rindex-1] < num:
            answer.append(num)
            insort_right(reserved, num)
        else:
            prev = rindex - 1
            for j in range(rindex, len(reserved)):
                if reserved[prev] + 1 == reserved[j]:
                    prev = j
                else:
                    answer.append(reserved[prev] + 1)
                    insort_right(reserved, reserved[prev] + 1)
                    break
            else:
                answer.append(reserved[len(reserved) - 1] + 1)
                insort_right(reserved, reserved[len(reserved) - 1] + 1)

    return answer


if __name__ == '__main__':
    result = solution(10, [1, 3, 4, 1, 3, 1])
    print(f'result = {result}')
    assert result == [1, 3, 4, 2, 5, 6]


