# -*- coding: utf-8 -*-
"""
방문 길이 : https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
"""


def solution(dirs):
    answer = 0
    dx = {"U" : 0, "D" : 0, "R" : 1, "L" : -1}
    dy = {"U" : -1, "D" : 1, "R" : 0, "L" : 0}

    prev = (0, 0)
    footprint = set()

    for d in dirs:
        _x, _y = prev
        x = _x + dx[d]
        y = _y + dy[d]

        if -5 <= x <= 5 and -5 <= y <= 5:
            foot = tuple(sorted([(_x, _y), (x, y)]))
            footprint.add(foot)
            prev = (x, y)

    answer = len(footprint)

    return answer


if __name__ == '__main__':
    result = solution("ULURRDLLU")
    print(f'result = {result}')
    assert result == 7

    result = solution("LULLLLLLU")
    print(f'result = {result}')
    assert result == 7
