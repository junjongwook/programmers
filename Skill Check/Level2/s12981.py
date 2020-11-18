# -*- coding: utf-8 -*-
"""
영어 끝말잇기 : https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3
"""


def solution(n, words):
    answer = [1, 1]
    temp = []
    for word in words:
        if len(temp) < 1:
            temp.append(word)
            continue
        answer[0] = answer[0] + 1
        if answer[0] > n :
            answer[0] = 1
            answer[1] = answer[1] + 1
        if word not in temp and temp[-1][-1] == word[0]:
            temp.append(word)
            continue
        break
    else:
        answer = [0, 0]

    return answer


if __name__ == '__main__':
    # result = solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
    # print(f'result = {result}')
    # assert result == [0, 0]

    result = solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
    print(f'result = {result}')
    assert result == [3, 3]