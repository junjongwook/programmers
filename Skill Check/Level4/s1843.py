# -*- coding: utf-8 -*-
"""
사칙연산 : https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3
"""

def solution(arr):
        maxMemory = dict()
        minMemory = dict()

        def calc(arr3):
            # print(f'calc arr3 = {arr3}')
            a, op, b = int(arr3[0]), arr3[1], int(arr3[2])
            if op == '+':
                return a + b
            elif op == '-':
                return a - b

        def MAX(arr):
            # print(f'MAX arr = {arr}')
            if len(arr) == 1: return int(arr[0])
            if len(arr) == 3: return calc(arr)

            key = ''.join(arr)
            if key in maxMemory:
                return maxMemory[key]

            _max = -float('inf')
            for i in range(1, len(arr)-1, 2):
                # print(f'MAX i = {i}, arr = {arr}')
                if arr[i] == '+':
                    _temp = MAX(arr[:i]) + MAX(arr[i+1:])
                else:
                    _temp = MAX(arr[:i]) - MIN(arr[i+1:])
                if _temp > _max: _max = _temp

            maxMemory[key] = _max

            return _max

        def MIN(arr):
            # print(f'MIN arr = {arr}')
            if len(arr) == 1: return int(arr[0])
            if len(arr) == 3: return calc(arr)

            key = ''.join(arr)
            if key in minMemory:
                return minMemory[key]

            _min = float('inf')
            for i in range(1, len(arr)-1, 2):
                if arr[i] == '+':
                    _temp = MIN(arr[:i]) + MIN(arr[i+1:])
                else:
                    _temp = MIN(arr[:i]) - MAX(arr[i+1:])
                if _temp < _min: _min = _temp

            minMemory[key] = _min

            return _min

        answer = MAX(arr)

        return answer


if __name__ == '__main__':
    result = solution(["1", "-", "3", "+", "5", "-", "8"])
    print(f'result = {result}')
    assert result == 1

    result = solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
    print(f'result = {result}')
    assert result == 3