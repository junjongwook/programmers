# -*- coding: utf-8 -*-
'''
멀쩡한 사각형 : https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
풀이 : https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
'''


def solution(w,h):
    from math import gcd
    answer = w * h - w - h + gcd(w, h)
    return answer


if __name__ == '__main__':
    result = solution(8, 12)
    print(f'result = {result}')
    assert result == 80