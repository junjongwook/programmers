# -*- coding: utf-8 -*-
'''
풍선 터트리기 : https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3
'''


def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 0  # 맨 앞과 맨 뒤는 무조건 가능하다
    # 오른쪽에서 시작해서 작은 값들은 제거해서 개수를 줄여 본다.
    length = len(a)
    left_min = a[0]
    right_min = a[length-1]

    left_min_mark = [0] * length    # 해당 값의 좌측에 보다 작은 값이 존재하는지?
    right_min_mark = [0] * length   # 해당 값의 우측에 보다 작은 값이 존재하는지?

    for i in range(length-1):
        if a[i+1] > left_min:
            left_min_mark[i+1] = 1
        else:
            left_min = a[i+1]

        if a[length - 2 - i] > right_min:
            right_min_mark[length - 2 - i] = 1
        else:
            right_min = a[length - 2 - i]

    for i in range(length):
        if left_min_mark[i] and right_min_mark[i]:
            continue
        else:
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution([9,-1,-5])
    print(f'result = {result}')
    assert result == 3

    result = solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
    print(f'result = {result}')
    assert result == 6