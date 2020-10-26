# -*- coding: utf-8 -*-
'''
문자열의 아름다움 : https://programmers.co.kr/learn/courses/30/lessons/68938
'''


def solution(s):
    answer = -1
    n = len(s)
    point = [[0] * n for _ in range(n)]
    for _s in range(n): # 부분 문자열의 시작 위치
        for _e in range(_s, n): # 부분 문자열의 끝 위치
            if _s == _e: continue   # 같은 위치를 가르키면 0
            if s[_s] != s[_e]:      # 최대 거리의 값들이 다르면 그 거리만큼
                point[_s][_e] = _e - _s
                continue
            _max = _e - _s - 1      # 최대 거리 보다 하나 아래부터
            _pre = point[_s][_e-1]  # 이전 최대 거리 값보다는 크거나 같을 거라
            check = False           # 최대 거리를 찾는지?
            for _l in range(_max, _pre, -1):    # 거리를 좁혀 가면서...
                for _s2 in range(_s, _e - _l):
                    if s[_s2] != s[_s2 + _l]:
                        point[_s][_e] = _l
                        check = True
                        break
                if check: break
            if not check:
                point[_s][_e] = _pre

    answer = sum([sum(p) for p in point])
            
    return answer


if __name__ == '__main__':
    result = solution("baby")
    print(f'result = {result}')
    assert result == 9

    result = solution("oo")
    print(f'result = {result}')