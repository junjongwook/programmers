# -*- coding: utf-8 -*-
"""
튜플 : https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
"""


def solution(s):
    answer = []
    s2 = list(eval(s[1:-1]))
    if len(s2) == 1: return s2
    s2.sort(key=len)
    for _s in s2:
        for _s2 in list(_s):
            if _s2 not in answer:
                answer.append(_s2)
                break

    return answer


if __name__ == '__main__':
    result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    print(f'result = {result}')
    assert result == [2, 1, 3 ,4]

    result = solution("{{123}}")
    print(f'result = {result}')
    assert result == [123]