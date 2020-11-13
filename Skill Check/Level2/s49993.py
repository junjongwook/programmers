# -*- coding: utf-8 -*-
'''
스킬트리 : https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3#fnref1
'''


def solution(skill, skill_trees):
    answer = 0
    d = dict()
    for i, s in enumerate(skill):
        d[s] = i

    for s in skill_trees:
        curr = -1
        check = True
        for _s in s:
            if _s not in d: continue
            index = d[_s]
            if index == curr + 1:
                curr = index
            else:
                check = False
                break
        if check:
            answer += 1

    return answer


if __name__ == '__main__':
    result = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
    print(f'result = {result}')
    assert result == 2

