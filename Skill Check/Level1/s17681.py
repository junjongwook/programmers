# -*- coding: utf-8 -*-
"""
[1차]비밀지도 : https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
"""


def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = a1 | a2
        f = '{:0' + str(n) + 'b}'
        answer.append(f.format(a).replace('0', ' ').replace('1', '#'))

    return answer


if __name__ == '__main__':
    result = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
    print(f'result = {result}')
    assert result == ["#####", "# # #", "### #", "#  ##", "#####"]