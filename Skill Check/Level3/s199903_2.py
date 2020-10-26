# -*- coding: utf-8 -*-


def solution(m, n, puddles):
    BASE = 1_000_000_007
    ground = [[0] * (m + 1) for _ in range(n + 1)]
    check = True
    for i in range(2, m + 1):
        if check:
            if [i, 1] in puddles:
                check = False
            else:
                ground[1][i] = 1

    check = True
    for j in range(2, n + 1):
        if check:
            if [1, j] in puddles:
                check = False
            else:
                ground[j][1] = 1

    for _n in range(2, n + 1):
        for _m in range(2, m + 1):
            if [_m, _n] in puddles:
                continue
            ground[_n][_m] = ( ground[_n][_m - 1] + ground[_n - 1][_m] ) % BASE

    answer = ground[n][m]
    return answer


if __name__ == '__main__':
    result = solution(4, 3, [[2, 2]])
    print(f'result={result}')
    assert result == 4

