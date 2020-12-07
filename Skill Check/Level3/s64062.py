# -*- coding: utf-8 -*-
"""
징검다리 건너기 : https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3
"""


def solution(stones, k):
    answer = 0
    while True:
        _k = k
        for i, s in enumerate(stones):
            if s == 0:
                _k = _k - 1
                if _k == 0:
                    break
            else:
                _k = k
                stones[i] -= 1
        else:
            answer += 1
            continue
        break

    return answer


if __name__ == '__main__':
    result = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    print(f'result = {result}')
    assert result == 3

