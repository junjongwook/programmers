# -*- coding: utf-8 -*-
"""
최적의 행렬 곱셈 : https://programmers.co.kr/learn/courses/30/lessons/12942?language=python3
"""

M = dict()
def solution(matrix_sizes):

    def MIN(i1, i2):
        if i1 == i2:
            return 0
        if (i1, i2) in M:
            return M[(i1, i2)]
        if i1 + 1 == i2:
            M[(i1, i2)] = matrix_sizes[i1][0] * matrix_sizes[i1][1] * matrix_sizes[i2][1]
            return M[(i1, i2)]

        _min = float('inf')
        for i in range(i1, i2):
            _sum = MIN(i1, i) + MIN(i + 1, i2) + matrix_sizes[i1][0] * matrix_sizes[i][1] * matrix_sizes[i2][1]
            if _sum < _min:
                _min = _sum

        M[(i1, i2)] = _min
        return M[(i1, i2)]

    answer = MIN(0, len(matrix_sizes) - 1)

    return answer


if __name__ == '__main__':
    result = solution([[5,3],[3,10],[10,6]])
    print(f'result = {result}')
    assert result == 270