# -*- coding: utf-8 -*-
'''
풍선 터트리기 : https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3
'''

def solution(a):
    answer = 0
    for _a in a:    # 살아 남을 수 있는지 판단할 숫자
        temp = a.copy()
        chance = 1          # 더 작은 것을 삭제할 기회는 한번뿐!
        if min(a) == _a:    # 제일 작은 수라면 무조건 남을 수 있다.
            answer += 1
            continue
        index = temp.index(_a)  # 살아 남아야할 숫자를 기준으로 좌우측의 최소 숫자를 정리한다.
        _left = temp[:index]
        _right = temp[index+1:]
        if _left and _right and max(min(_left), _a, min(_right)) == _a: # 살아 남을 수 없다.
            pass
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