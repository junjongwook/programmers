# -*- coding: utf-8 -*-
'''
3진법 뒤집기 : https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
'''


def solution(n):
    answer = 0
    temp = []
    while n > 0:
        _n = n % 3
        n = n // 3
        temp.append(_n)

    for _n in temp:
        answer = answer * 3 + _n

    return answer


if __name__ == '__main__':
    result = solution(45)
    print(f'result = {result}')
    assert result == 7

    result = solution(125)
    print(f'result = {result}')
    assert result == 229

