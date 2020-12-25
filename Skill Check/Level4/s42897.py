# -*- coding: utf-8 -*-
"""
도둑질 : https://programmers.co.kr/learn/courses/30/lessons/42897
"""
from collections import deque

def solution(money):
    answer = 0
    if len(money) == 1: return money[0]
    if len(money) == 2: return max()
    if len(money) == 3: return max(money)

    width = len(money)
    # 첫번째 집을 방문했을 경우는 마지막 집은 방문하지 않는다.
    queue = deque([(money[0], 1)])
    for i in range(1, width - 1):
        _queue = deque([])
        while queue:
            q, v = queue.popleft()
            if v == 1:
                _queue.append((q, 0))
            else:
                _queue.append((q, 0))
                if money[i] > 0:    # 돈이 없는 집은 방문하지 않는다.
                    _queue.append((q + money[i], 1))
        queue = _queue
    answer = max(queue)[0]

    # 첫번째 집을 방문하지 않았을 경우는 마지막 집을 방문할 수 있다.
    queue = deque([(money[1], 1)])
    for i in range(2, width):
        _queue = deque([])
        while queue:
            q, v = queue.popleft()
            if v == 1:
                _queue.append((q, 0))
            else:
                _queue.append((q, 0))
                if money[i] > 0:    # 돈이 없는 집은 방문하지 않는다.
                    _queue.append((q + money[i], 1))
        queue = _queue

    answer = max(answer, max(queue)[0])

    return answer

if __name__ == '__main__':
    result = solution([1, 2, 3, 1])
    print(f'result = {result}')
    assert result == 4

    result = solution([1, 2, 1, 1, 5])
    print(f'result = {result}')
    assert result == 7
