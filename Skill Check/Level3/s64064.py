# -*- coding: utf-8 -*-
"""
불량 사용자 : https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
"""

import re
from collections import deque


def solution(user_id, banned_id):
    answer = 0

    banned_pattern = [re.compile('^' + a.replace('*', '.') + '$') for a in banned_id]
    sanction = []
    for p in banned_pattern:
        temp = list(filter(p.match, user_id))
        sanction.append(temp)

    queue = deque([()])
    width = len(banned_pattern)
    # print(f'width = {width}')
    banned_list = []
    while queue:
        banned_ids = queue.popleft()
        # print(f'banned_ids = {banned_ids}')
        if len(banned_ids) == width:
            temp = set(banned_ids)
            if len(temp) < width:
                pass
            elif temp not in banned_list:
                banned_list.append(temp)
            else:
                pass
            continue

        index = len(banned_ids)
        for id in sanction[index]:
            queue.append(banned_ids + (id,))
    # print(f'banned_list = {banned_list}')
    answer = len(banned_list)

    return answer


if __name__ == '__main__':
    result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
    print(f'result = {result}')
    assert result == 2

    result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
    print(f'result = {result}')
    assert result == 2

    result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
    print(f'result = {result}')
    assert result == 3