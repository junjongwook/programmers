# -*- coding: utf-8 -*-
"""
보석 쇼핑 : https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
"""


def solution(gems):
    width = len(gems)
    d = dict()
    for g in gems:
        d.setdefault(g, 0)
        d[g] += 1
    d2 = d.copy()

    answer = [1, width - 1]

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

    # 앞에서부터 자르는 걸 먼저 해 본다.
    start2 = 1
    for i in range(0, width):
        if d2[gems[i]] == 1:
            start2 = i + 1
            break
        else:
            d2[gems[i]] -=1
    # 뒤에서 자르는 걸 해 본다.
    end2 = width
    for j in range(width - 1, -1, -1):
        if d2[gems[j]] == 1:
            end2 = j + 1
            break
        else:
            d2[gems[j]] -= 1

    if end2 - start2 < end - start:
        answer = [start2, end2]
    else:
        answer = [start, end]

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