# -*- coding: utf-8 -*-
"""
[3차] 압축 : https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3
"""


def solution(msg):
    answer = []
    사전 = dict()
    import string
    for i, s in enumerate(string.ascii_uppercase, 1):
        사전[s] = i

    lastIndex = 27
    from collections import deque
    queue = deque(msg)
    word = ''
    while queue:
        word = word + queue.popleft()
        if word in 사전:
            continue
        else:
            prev = word[:-1]
            answer.append(사전[prev])
            사전[word] = lastIndex
            lastIndex += 1
            # answer.append(사전[word])
            word = word[-1]
    if word in 사전:
        answer.append(사전[word])

    return answer


if __name__ == '__main__':
    result = solution("KAKAO")
    print(f'result = {result}')
    assert result == [11, 1, 27, 15]