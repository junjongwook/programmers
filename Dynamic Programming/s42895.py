# -*- coding: utf-8 -*-
'''
N으로 표현 : https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
'''

def solution(N, number):
    if N == number: return 1
    temp = [{}]         # 0 인덱스는 사용하지 않는다.
    temp.append({N})    # 한 개로 할 수 있는 건 하나뿐
    for n in range(2, 9):
        start, end = 1, n - 1
        _N = int(str(N) * n)
        if _N == number:
            return n
        temp2 = set([_N])
        while start <= end:
            _temp1 = temp[start]
            _temp2 = temp[end]

            for _n1 in _temp1:
                for _n2 in _temp2:
                    _add = _n1 + _n2
                    _minus1 = _n1 - _n2
                    _minus2 = _n2 - _n1
                    _multiply = _n1 * _n2
                    if _n2 != 0: _divide1 = _n1 / _n2
                    if _n1 != 0: _divide2 = _n2 / _n1
                    temp2 = temp2.union(set([_add, _minus1, _minus2, _multiply, _divide1, _divide2]))
                    if number in temp2:
                        return n

            start = start + 1
            end = end - 1

        temp.append(temp2)

    return -1


if __name__ == '__main__':

    result = solution(5, 5)
    print(f'result = {result}')
    assert result == 1

    result = solution(5, 55)
    print(f'result = {result}')
    assert result == 2

    result = solution(5, 12)
    print(f'result = {result}')
    assert result == 4

    result = solution(2, 11)
    print(f'result = {result}')
    assert result == 3