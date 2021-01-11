# -*- coding: utf-8 -*-
"""
문자열의 아름다움 : https://programmers.co.kr/learn/courses/30/lessons/68938?language=python3
"""
import sys
sys.setrecursionlimit(10**6)

d = dict()
answer = 0
def solution(s):
    global d, answer
    answer = 0
    d = dict()
    N = len(s)

    def segment(_s, _e):
        global d, answer
        if _s == _e: return 0   # 등록하지 않음
        if (_s, _e) in d:
            return d[(_s, _e)]

        if s[_s] != s[_e]:
            _count = _e - _s
            segment(_s, _e - 1)
            segment(_s + 1, _e)
        else:
            _count = max(segment(_s, _e - 1), segment(_s + 1, _e))
        d[(_s, _e)] = _count
        answer += _count

        return _count

    segment(0, N-1)
    # print(f'd = {d}')
    # answer = sum(d.values())

    return answer


if __name__ == '__main__':
    result = solution("baby")
    print(f'result = {result}')
    assert result == 9

    result = solution("oo")
    print(f'result = {result}')
    assert result == 0

    result = solution("abb")
    print(f'result = {result}')
    assert result == 3

