# -*- coding: utf-8 -*-
"""
선입 선출 스케쥴링 : https://programmers.co.kr/learn/courses/30/lessons/12920?language=python3
"""


def solution(n, cores):
    answer = 0
    N = len(cores)

    process = [0] * N
    while n > 0:
        for i in range(N):
            if process[i] == 0:
                process[i] = cores[i]
                n = n - 1
                if n == 0:
                    return i + 1
        # 시간을 한번 흘려 보냄
        for i in range(N):
            process[i] -= 1

    return answer


if __name__ == '__main__':
    result = solution(6, [1,2,3])
    print(f'result = {result}')
    assert result == 2
