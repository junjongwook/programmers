# -*- coding: utf-8 -*-
"""
보석 쇼핑 : https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
"""


def solution(gems):
    width = len(gems)
    d = dict()
    for g in gems:  # 개별 보석의 개수 초기화
        d[g] = 0

    answer = [0, width - 1]
    left, right = 0, 0
    d[gems[0]] = 1
    while left <= right and right < width:
        if 0 not in d.values():
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
            d[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right < width:
                d[gems[right]] += 1

    answer = [answer[0] + 1, answer[1] + 1]
    return answer


if __name__ == '__main__':
    result = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    print(f'result = {result}')
    assert result == [3, 7]

    result = solution(["AA", "AB", "AC", "AA", "AC"])
    print(f'result = {result}')
    assert result == [1, 3]

    result = solution(["XYZ", "XYZ", "XYZ"])
    print(f'result = {result}')
    assert result == [1, 1]

    result = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
    print(f'result = {result}')
    assert result == [1, 5]

    result = solution(["A", "A", "B"])
    print(f'result = {result}')
    assert result == [2, 3]

    result = solution(["A", "B", "A"])
    print(f'result = {result}')
    assert result == [1, 2]

    result = solution( ["DIA", "EM", "EM", "RUB", "DIA"])
    print(f'result = {result}')
    assert result == [3, 5]