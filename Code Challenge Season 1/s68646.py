# -*- coding: utf-8 -*-
'''
풍선 터트리기 : https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3
'''

def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 2
    left_min = a[0]
    right_min = min(a[1:])
    for i in range(1, len(a) - 1):
        if max(left_min, a[i], right_min) == a[i]:
            pass
        else:
            answer = answer + 1
        left_min = min(left_min, a[i])
        if right_min == a[i+1] and i < len(a) - 2:
            right_min = min(a[i+2:])

    return answer


if __name__ == '__main__':
    result = solution([9,-1,-5])
    print(f'result = {result}')
    assert result == 3

    result = solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
    print(f'result = {result}')
    assert result == 6