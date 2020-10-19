# -*- coding : utf-8 -*-
'''
타겟 넘버 : https://programmers.co.kr/learn/courses/30/lessons/43165
'''


def solution(numbers, target):
    from collections import deque
    answer = 0
    queue = deque([0])
    for n in numbers:
        temp_queue = deque([])
        while queue:
            temp = queue.popleft()
            temp_queue.append(temp + n)
            temp_queue.append(temp - n)
        queue = temp_queue

    while queue:
        _sum = queue.popleft()
        if _sum == target:
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution([1, 1, 1, 1, 1], 3)
    print(f'result = {result}')
    assert result == 5

