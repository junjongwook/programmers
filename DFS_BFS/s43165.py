# -*- coding : utf-8 -*-
'''
타겟 넘버 : https://programmers.co.kr/learn/courses/30/lessons/43165
'''


def solution(numbers, target):
    answer = 0
    queue = [0]
    for n in numbers:
        temp_queue = []
        while queue:
            temp = queue.pop(0)
            temp_queue.append(temp + n)
            temp_queue.append(temp - n)
        queue = temp_queue

    while queue:
        _sum = queue.pop(0)
        if _sum == target:
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution([1, 1, 1, 1, 1], 3)
    print(f'result = {result}')
    assert result == 5

