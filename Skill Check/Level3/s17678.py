# -*- coding: utf-8 -*-
"""
[1차]셔틀버스 : https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
"""
from bisect import bisect_right

def solution(n, t, m, timetable):
    # print(f'n = {n}, t = {t}, m = {m}, timetable = {timetable}')
    answer = ''
    busStart = 9 * 60   # "09:00"
    busEnd = busStart + (n - 1) * t
    busTime = [b for b in range(busStart, busEnd + 1, t)]

    # print(f'busTime = {busTime}')
    def timeToNumber(s):
        return int(s[:2]) * 60 + int(s[3:])

    def numberToTime(n):
        h = n // 60
        m = n % 60
        return f'{h:02}:{m:02}'

    crueTime = [timeToNumber(t) for t in timetable]
    crueTime.sort()
    # print(f'curTime = {crueTime}')

    last = []
    for b in busTime:
        index = bisect_right(crueTime, b)
        if index <= m:
            last = crueTime[:index]
            crueTime = crueTime[index:]
        else:
            last = crueTime[:m]
            crueTime = crueTime[m:]

    # print(f'last = {last}')
    if len(last) < m:
        answer = numberToTime(busEnd)
    else:
        answer = numberToTime(last[-1] - 1)

    return answer


if __name__ == '__main__':
    result = solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
    print(f'result = {result}')
    assert result == "09:00"

    result = solution(2, 10, 2, ["09:10", "09:09", "08:00"])
    print(f'result = {result}')
    assert result == "09:09"

    result = solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
    print(f'result = {result}')
    assert result == "08:59"

    result = solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
    print(f'result = {result}')
    assert result == "00:00"

    result = solution(1, 1, 1, ["23:59"])
    print(f'result = {result}')
    assert result == "09:00"

    result = solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
    print(f'result = {result}')
    assert result == "18:00"
