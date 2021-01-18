# -*- coding: utf-8 -*-
"""
폰켓몬 : https://programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    answer = 0
    _nums = set(nums)

    answer = min(len(nums) // 2, len(_nums))
    return answer


if __name__ == '__main__':
    result = solution([3,1,2,3])
    print(f'result = {result}')
    assert result == 2
