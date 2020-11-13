# -*- coding: utf-8 -*-
'''
이진 변환 반복하기
'''

def solution(s):
    answer = []

    count = 0
    deleted = 0
    while s != '1':
        count = count + 1
        _s = s.count("1")
        deleted = deleted + len(s) - _s
        s = '{:b}'.format(_s)
    answer = [count, deleted]

    return answer


if __name__ == '__main__':
    result = solution("110010101001")
    print(f'result = {result}')
    assert result == [3, 8]

    result = solution("01110")
    print(f'result = {result}')
    assert result == [3, 3]

    result = solution("1111111")
    print(f'result = {result}')
    assert result == [4, 1]

