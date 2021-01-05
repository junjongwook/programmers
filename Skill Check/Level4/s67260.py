# -*- coding: utf-8 -*-
"""
동굴 탐험 : https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3
"""


def solution(n, path, order):
    answer = False
    pre = dict()
    nxt = dict()
    for _p, _n in order:
        pre[_n] = _p
        nxt[_p] = _n
    if 0 in pre: return False   # 0 의 선입 조건이 있으면 실패
    adjacent = dict()
    for ad1, ad2 in path:
        adjacent.setdefault(ad1, [])
        adjacent.setdefault(ad2, [])
        adjacent[ad1].append(ad2)
        adjacent[ad2].append(ad1)

    prison = set()
    visited = set()

    stack = [0]
    visited.add(0)
    while stack:
        curr = stack.pop()
        candidates = adjacent[curr]
        for c in candidates:
            if c in visited: continue       # 기존에 방문했던 곳이면 통과
            # 선행 조건이 필요한지 확인
            if c in pre and pre[c] not in visited:  # 선행 조건이 있고, 그게 아직 방문 전이라면 구치소로..
                prison.add(c)
                continue
            else:
                visited.add(c)
                stack.append(c)
        # 현재 값이 다른 값의 선행 조건이고, 그 선행 조건이 구치소에 있다면 탈출 시켜 주자.
        if curr in nxt and nxt[curr] in prison:
            prison.discard(nxt[curr])
            visited.add(nxt[curr])
            stack.append(nxt[curr])

        # 방문 장소가 모두 n 개가 된다면 어떻게 하든 모두 갈 수 있다는 거니까...
        if len(visited) == n: return True

    return answer


if __name__ == '__main__':
    result = solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])
    print(f'result = {result}')
    assert result == True

    result = solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]])
    print(f'result = {result}')
    assert result == True

    result = solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])
    print(f'result = {result}')
    assert result == False

