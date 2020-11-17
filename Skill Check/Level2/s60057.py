# -*- coding: utf-8 -*-
'''
문자열 압축 : https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
'''


def solution(s):
    length = len(s)
    answer = length
    answerStr = s

    def encode(pi):
        prev = s[:pi]
        temp = []
        count = 0
        length2 = length // pi * pi
        rest = s[length2:]
        for i in range(0, length2, pi):
            if s[i:i+pi] == prev:
                count = count + 1
            else:
                temp.append(str(count) if count > 1 else '')
                temp.append(prev)
                prev = s[i:i+pi]
                count = 1
        temp.append(str(count) if count > 1 else '')
        temp.append(prev)
        temp.append(rest)

        return ''.join(temp)

    for i in range(1, length//2 + 1):
        temp = encode(i)
        if len(temp) < answer:
            answer, answerStr = len(temp), temp

    return answer


if __name__ == '__main__':
    # result = solution("aabbaccc")
    # print(f'result = {result}')
    # assert result == 7

    # result = solution("ababcdcdababcdcd")
    # print(f'result = {result}')
    # assert result == 9

    result = solution("abcabcdede")
    print(f'result = {result}')
    assert result == 8



