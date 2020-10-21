# -*- coding: utf-8 -*-
'''
풍선 터트리기 : https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3
'''

def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 2
    left_min = a[0]
    right_min = None # 필요할 때만 min 을 수행한다.
    for i in range(1, len(a) - 1):
        if left_min > a[i]: # 왼쪽이 모두 다 크면 그냥 오른쪽은 비교할 필요도 없다.
            answer += 1
            left_min = a[i]
            continue
        else:   # 이제 오른쪽을 찾아 봐야 하는구나
            right_min = min(a[i+1:])
            if right_min > a[i]: # 이러면 성공!
                answer += 1

    return answer


if __name__ == '__main__':
    result = solution([9,-1,-5])
    print(f'result = {result}')
    assert result == 3

    result = solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
    print(f'result = {result}')
    assert result == 6