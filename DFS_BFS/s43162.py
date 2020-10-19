# -*- coding: utf-8 -*-

def solution(n, computers):
    answer = 0
    temp = list(range(n))

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and temp[i] > temp[j]:
                temp[i] = temp[j]

    answer = len(set(temp))

    return answer


if __name__ == '__main__':
    result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(f'result = {result}')
    assert result == 2

    result = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    print(f'result = {result}')
    assert result == 1
    
    result = solution(6, [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]])
    print(f'result = {result}')
    assert result == 1
