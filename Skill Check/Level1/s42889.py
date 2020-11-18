# -*- coding: utf-8 -*-
"""
실패율 : https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
"""


def solution(N, stages):
    answer = list(range(1, N+1))
    users = [0] * (N + 2)
    fail = [0] * (N + 2)
    for stage in stages:
        users[stage] += 1
    for i in range(1, N + 1):
        fail[i] = users[i] / sum(users[i:]) if sum(users[i:]) > 0 else 0

    answer.sort(key=lambda n: fail[n], reverse=True)

    return answer


if __name__ == '__main__':
    result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
    print(f'result = {result}')
    assert result == [3, 4, 2, 1, 5]

