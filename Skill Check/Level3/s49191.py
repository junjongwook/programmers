# -*- coding: utf-8 -*-
"""
순위 : https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
"""


def solution(n, results):
    answer = 0
    win = [[0] * (n+1) for _ in range(n+1)]
    lose = [[0] * (n+1) for _ in range(n+1)]
    for w, l in results:
        win[w][l] = 1
        lose[l][w] = 1

    _cont = True
    while _cont:
        _cont = False
        for s in range(1, n+1):
            for e in range(1, n+1):
                for b in range(1, n+1):
                    if s == e or e == b or e == s: continue
                    if win[s][b] == 1 and win[b][e] == 1 and win[s][e] == 0:
                        win[s][e] = 1
                        _cont = True
                    if lose[s][b] == 1 and lose[b][e] == 1 and lose[s][e] == 0:
                        lose[s][e] = 1
                        _cont = True
    winCount = [0] * (n+1)
    loseCount = [0] * (n+1)
    for i in range(1, n+1):
        winCount = sum(win[i])
        loseCount = sum(lose[i])
        if winCount + loseCount == n - 1:
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	)
    print(f'result = {result}')
    assert result == 2
