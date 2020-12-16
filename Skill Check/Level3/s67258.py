# -*- coding: utf-8 -*-
"""
보석 쇼핑 : https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
"""


def solution(gems):
    width = len(gems)
    answer = [0, width - 1]
    d = dict()
    for g in gems:
        d.setdefault(g, 0)
        d[g] += 1

    # 뒤에서 잘라본다.
    end = width
    for i in range(width - 1, -1, -1):
        if d[gems[i]] == 1:
            end = i + 1
            break
        else:
            d[gems[i]] -= 1

    # 이제는 앞에서 잘라본다.
    start = 1
    for j in range(0, width):
        if d[gems[j]] == 1:
            start = j + 1
            break
        else:
            d[gems[j]] -= 1

    return [start, end]


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