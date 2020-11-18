# -*- coding: utf-8 -*-
"""
예산 : https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
"""


def solution(d, budget):
    answer = 0
    d.sort()
    for _d in d:
        if budget >= _d:
            answer += 1
            budget -= _d
        else:
            break

    return answer