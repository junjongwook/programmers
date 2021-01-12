# -*- coding: utf-8 -*-
"""
문자열의 아름다움 : https://programmers.co.kr/learn/courses/30/lessons/68938?language=python3
"""


def solution(s):
    answer = 0
    d = dict()
    N = len(s)

    stack = [(0, N-1)]  # 0, N-1 일때의 최대값 구하기
    while stack:
        # print(f'd = {d}')
        # print(f'stack = {stack}')
        top = stack[-1]     # stack 의 맨 위의 값을 pop 하지 않고 참조

        if top in d:        # 이미 계산한 적이 있는 구간이면 pass
            stack.pop()
            continue

        if top[1] - top[0] == 1:   # 길이가 2개인 구간은 바로 계산할 수 있다. 0 아니면 1이다.
            stack.pop()
            if s[top[0]] == s[top[1]]:
                d[top] = 0
            else:
                d[top] = 1
            answer = answer + d[top]
            continue

        left = (top[0], top[1] - 1)         # 좌측끝부터 시작하는 것 하나 분리
        right = (top[0] + 1, top[1])        # 우측끝까지 끝나는 것 하나 분리
        if left in d and right in d:        # 두 값 모두 계산이 완료되어 있으면 
            stack.pop()
            if s[top[0]] == s[top[1]]:      # 현재 거의 최대 길이가 존재하는지 확인
                d[top] = max(d[left], d[right])   # 없다면 아래 두 개 중의 최대값을 선택
            else:
                d[top] = top[1] - top[0]
            answer = answer + d[top]
            continue

        # 처리가 안되면 right, left 를 stack 다시 넣어 둔다.
        if right not in d:
            stack.append(right)
        if left not in d:
            stack.append(left)

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

