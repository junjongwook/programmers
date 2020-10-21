# -*- coding: utf-8 -*-
'''
쿼드압축 후 개수 세기 : https://programmers.co.kr/learn/courses/30/lessons/68936?language=python3
'''


def solution(arr):
    if len(arr) == 1:
        if arr[0][0] == 1: return [0, 1]
        else: return [1, 0]
    answer = [0, 0]
    stack = [arr]

    def _4분할(arr2):
        length = len(arr2)
        width = length // 2
        _1square = [arr2[i][:width] for i in range(width)]
        _2square = [arr2[i][width:] for i in range(width)]
        _3square = [arr2[i][:width] for i in range(width, length)]
        _4square = [arr2[i][width:] for i in range(width, length)]

        return [_1square, _2square, _3square, _4square]
    while stack:
        temp = stack.pop()
        if len(temp) == 1:
            answer[temp[0][0]] += 1
            continue
        _prev = temp[0][0]
        check = True
        for i in range(len(temp)):
            for j in range(len(temp)):
                if _prev != temp[i][j]:
                    check = False
                    break
            if not check:
                break
        if check:
            answer[_prev] += 1
            continue

        _분할목록 = _4분할(temp)
        for _분할 in _분할목록:
            stack.append(_분할)

    return answer


if __name__ == '__main__':
    result = solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
    print(f'result = {result}')
    assert result == [4,9]

    result = solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
    print(f'result = {result}')
    assert result == [10,15]