# -*- coding: utf-8 -*-
"""
도둑질 : https://programmers.co.kr/learn/courses/30/lessons/42897
"""


def solution(money):
    answer = 0
    if len(money) == 1: return money[0]
    if len(money) == 2: return max()
    if len(money) == 3: return max(money)

    width = len(money)
    # 두번째 집부터 방문할 경우 끝집까지 갈 수 있다.
    q = {0: 0, 1: money[1]}    # 2번째 집(index : 1), 0 은 방문하지 않음, 1 : 방문함
    for i in range(2, width):
        # 바로 앞의 집을 방문하지 않은 경우의 값에 대해서
        notVisited = max(q[0], q[1])
        visited = q[0] + money[i]
        q = {0: notVisited, 1 : visited}
    answer = max(q[0], q[1])

    # 첫번째 집이 money 가 0이면 굳이 필요없다.
    if money[0] == 0:
        return answer

    # 첫번째 집부터 방문할 경우 끝집은 가지 않는다.
    q = {0: 0, 1: money[0]}
    for i in range(1, width - 1):
        notVisited = max(q[0], q[1])
        visited = q[0] + money[i]
        q = {0: notVisited, 1: visited}
    answer = max(answer, max(q[0], q[1]))

    return answer

if __name__ == '__main__':
    result = solution([1, 2, 3, 1])
    print(f'result = {result}')
    assert result == 4

    result = solution([1, 2, 1, 1, 5])
    print(f'result = {result}')
    assert result == 7
