# -*- coding: utf-8 -*-
"""
보석 쇼핑 : https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
"""


def solution(gems):
    width = len(gems)
    answer = [0, width-1]
    _max = len(set(gems))


    start = 0
    while start < width:
        # print(f'start = {start}')
        temp = set()
        for i in range(start, width):
            temp.add(gems[i])
            l = len(temp)
            if l == 1: start = i
            if l == _max:
                if answer[1] - answer[0] > i - start:
                    answer = [start, i]
                    break
        else:
            break

        start = start + 1

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