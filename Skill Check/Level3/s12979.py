# -*- coding: utf-8 -*-
"""
기지국 설치 : https://programmers.co.kr/learn/courses/30/lessons/12979
"""


def solution(n, stations, w):
    term = []
    prev = 0 - w
    end = n + w + 1
    stations.append(end)
    for s in stations:
        _d = s - prev - 2 * w - 1
        prev = s
        if _d > 0:
            term.append(_d)

    answer = 0
    for t in term:
        answer += (t // (2*w + 1)) + (0 if t % (2*w + 1) == 0 else 1)

    return answer


if __name__ == '__main__':
    result = solution(11, [4, 11], 1)
    print(f'result = {result}')
    assert result == 3


