# -*- coding: utf-8 -*-
"""
오픈채팅방 : https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
"""


def solution(records):
    answer = []
    nameDict = dict()
    actions = []
    for record in records:
        action, *user = record.split()
        actions.append((action, user[0]))
        if len(user) > 1:
            nameDict[user[0]] = user[1]

    for action, user in actions:
        if action == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(nameDict[user]))
        elif action == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(nameDict[user]))
    return answer


if __name__ == '__main__':
    result = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
    print(f'result = {result}')
    assert result == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
