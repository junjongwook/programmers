# -*- coding: utf-8 -*-
"""
[1차]추석 트래픽 : https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
"""

import bisect
def solution(lines):
    data = []
    points = set()
    for line in lines:
        _e = line[11:23]
        e = int(_e[0:2]) * 60 * 60 + int(_e[3:5]) * 60 + int(_e[6:8])
        e = e * 1000 + int(_e[-3:])
        elapsed = int(float(line[24:][:-1]) * 1000)
        s = e - elapsed + 1
        bisect.insort(data, (s, e))
        points.add(s)
        points.add(e)
    points = sorted(points)

    answer = 0
    for point in points:
        _s = point
        _e = point + 1000 - 1
        temp = [d for d in data if _s <= d[0] <= _e or _s <= d[1] <= _e or (d[0] <= _s and d[1] >= _e)]
        if len(temp) > answer:
            answer = len(temp)

    return answer


if __name__ == '__main__':
    result = solution(["2016-09-15 00:00:00.000 3s"])
    print(f'result = {result}')
    assert result == 1

    result = solution(["2016-09-15 23:59:59.999 0.001s"])
    print(f'result = {result}')
    assert result == 1

    result = solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
    print(f'result = {result}')
    assert result == 1

    result = solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
    print(f'result = {result}')
    assert result == 2

    result = solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
    print(f'result = {result}')
    assert result == 7

    result = solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])
    print(f'result = {result}')
    assert result == 1