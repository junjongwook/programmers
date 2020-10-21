# -*- coding: utf-8 -*-
'''
풍선 터트리기 : https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3
'''

import heapq, bisect


def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 2  # 맨 앞과 맨 뒤는 무조건 가능하다
    # 오른쪽에서 시작해서 작은 값들은 제거해서 개수를 줄여 본다.
    length = len(a)
    left_min = a[0]
    right_under = a[length-1]
    right_under_index = length - 1

    for i in range(1, length - 1):
        if left_min > a[i]: # 왼쪽에 작은 값이 없으면
            answer += 1
            left_min = a[i]
            continue
        elif i < right_under_index and a[i] > right_under:  # 오른쪽에 작은 값이 있으면
            continue
        elif i < right_under_index: # 좀더 작은 값을 찾아 보려면
            _check = False
            for j in range(right_under_index - 1, i, -1):
                if a[j] < a[i]: # 작은 값이 존재하면
                    right_under_index = j
                    right_under = a[j]
                    _check = True
                    break
            if _check: # 작은 값을 찾았으니
                continue
            else: # 오른쪽에 작은 값이 없으면
                answer += 1
                continue
        else:   # 오른쪽의 작은값을 다시 찾아야 하는 경우
            _check = False
            for j in range(length - 1, i, -1):
                if a[j] < a[i]:
                    right_under_index = j
                    right_under = a[j]
                    _check = True
                    break
            if _check: # 작은 값을 찾았으니
                continue
            else:       # 오른쪽에 작은 값이 없으면
                answer += 1
                continue

    return answer


if __name__ == '__main__':
    result = solution([9,-1,-5])
    print(f'result = {result}')
    assert result == 3

    result = solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
    print(f'result = {result}')
    assert result == 6