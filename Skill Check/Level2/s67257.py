# -*- coding: utf-8 -*-
"""
수식 최대화 : https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
"""
import re
from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    _expression = re.findall('(\d+|[-*+])', expression)
    orders = list(permutations('+-*', 3))
    # print(_expression)
    # print(orders)

    for _orders in orders:
        queue = deque(_expression)
        for op in _orders:
            newQueue = deque([])
            while queue:
                q = queue.popleft()
                if q == op:
                    n1 = int(newQueue.pop())
                    n2 = int(queue.popleft())
                    if q == '+':
                        n3 = n1 + n2
                    elif q == '-':
                        n3 = n1 - n2
                    elif q == '*':
                        n3 = n1 * n2
                    newQueue.append(str(n3))
                else:
                    newQueue.append(q)
            queue = newQueue
        # print(f'newQueue = {newQueue}')
        answer = max(answer, abs(int(newQueue[0])))

    return answer


if __name__ == '__main__':
    result = solution("100-200*300-500+20")
    print(f'result = {result}')
    assert result == 60420

    result = solution("50*6-3*2")
    print(f'result = {result}')
    assert result == 300