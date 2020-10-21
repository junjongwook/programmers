# -*- coding: utf-8 -*-
'''
두 개 뽑아서 더하기 : https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
'''

def solution(numbers):
    answer = []
    for i1 in range(len(numbers)):
        for i2 in range(len(numbers)):
            if i1 == i2: continue
            answer.append(numbers[i1] + numbers[i2])

    answer = set(answer)
    answer = list(answer)
    answer.sort()

    return answer


if __name__ == '__main__':
    result = solution([2, 1, 3, 4, 1])
    print(f'result = {result}')
    assert result == [2, 3, 4, 5, 6, 7]

    result = solution([5, 0, 2, 7])
    print(f'result = {result}')
    assert result == [2, 5, 7, 9, 12]
