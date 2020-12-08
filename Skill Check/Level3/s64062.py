# -*- coding: utf-8 -*-
"""
징검다리 건너기 : https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3
"""


def solution(stones, k):
    answer = 0
    length = len(stones)
    _min, _max = min(stones), max(stones)
    while _min <= _max:
        _mid = (_min + _max) // 2
        zero = [0] * (length + 1)
        for i in range(1, length + 1):
            if stones[i-1] - _mid < 0:
                zero[i] = zero[i-1] + 1
                if zero[i] >= k:
                    _max = _mid - 1
                    break
        else:
            answer = _mid
            _min = _mid + 1

    return answer



if __name__ == '__main__':
    result = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    print(f'result = {result}')
    assert result == 3

