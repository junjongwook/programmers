# -*- coding: utf-8 -*-
"""
방의 개수 : https://programmers.co.kr/learn/courses/30/lessons/49190?language=python3
"""


def solution(arrows):
    answer = 0
    dxy = [
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    ]
    exist = set()   # 선들의 집합, 첫번째, 두번째 좌표를 정렬하면 하나만 있어도 되지 않을까?
    curr = (0, 0)   # x, y 좌표
    visited = set([curr]) # 방문한 좌표들
    for arrow in arrows:
        dx, dy = dxy[arrow]

        next = curr[0] + dx, curr[1] + dy
        edge = tuple(sorted([curr, next]))
        if next in visited and edge not in exist:
            answer += 1
        visited.add(next)
        exist.add(edge)
        curr = next
        # print(f'visited = {visited}, exist = {exist}')

        # 칸을 한칸이 아닌 두칸씩으로 설정해서 사용한다. 대각선 때문...
        next = curr[0] + dx, curr[1] + dy
        edge = tuple(sorted([curr, next]))
        if next in visited and edge not in exist:
            answer += 1
        visited.add(next)
        exist.add(edge)
        curr = next
        # print(f'visited = {visited}, exist = {exist}')

    return answer


if __name__ == '__main__':
    result = solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])
    print(f'result = {result}')
    assert result == 3

