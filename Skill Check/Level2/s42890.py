# -*- coding: utf-8 -*-
"""
후보키 : https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3
"""


def solution(relation):
    answer = 0
    columns = list(range(len(relation[0])))
    tuples = []
    from itertools import combinations
    for 튜플개수 in range(1, len(columns) + 1):
        for 튜플 in combinations(columns, 튜플개수):
            # 최소성 확인 - 이전 tuple 중에 있는지
            check = False
            for tuple in tuples:
                if len(set(tuple) & set(튜플)) == len(tuple):
                    check = True
                    break
            if check: continue
            temp = set()
            for r in relation:
                temp2 = ''
                for i in list(튜플):
                    temp2 += r[i]
                temp.add(temp2)
            if len(temp) == len(relation):
                tuples.append(튜플)

    answer = len(tuples)
    return answer


if __name__ == '__main__':
    result = solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
    print(f'result = {result}')
    assert result == 2

