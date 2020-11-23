# -*- coding: utf-8 -*-
"""
여행경로 : https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
"""

def solution(tickets):
    if len(tickets) == 1: return tickets[0]
    nextDict = dict()
    availableDict = dict()
    for prev, next in tickets:
        nextDict.setdefault(prev, [])
        availableDict.setdefault((prev, next), 0)
        nextDict[prev].append((prev, next))
        availableDict[(prev, next)] += 1

    route = []
    routeList = []
    def DFS(a):
        route.append(a)
        # print(f'route = {route}')
        if len(route) == len(tickets) + 1:
            routeList.append(route.copy())
            return

        if a in nextDict:
            nexts = nextDict[a]
            for next in nexts:
                if availableDict[next] > 0:
                    availableDict[next] -= 1
                    DFS(next[1])
                    route.pop()
                    availableDict[next] += 1

    DFS('ICN')

    routeList.sort()
    answer = routeList[0]

    return answer


if __name__ == '__main__':
    # result = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    # print(f'result = {result}')
    # assert result == ["ICN", "JFK", "HND", "IAD"]

    result = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    print(f'result = {result}')
    assert result == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

    result = solution([["ICN", "JFK"]])
    print(f'result = {result}')
    assert result == ["ICN", "JFK"]

    result = solution([["JFK", "ICN"], ["ICN", "JFK"]])
    print(f'result = {result}')
    assert result == ["ICN", "JFK", "ICN"]

    result = solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])
    print(f'result = {result}')
    assert result == ["ICN", "B", "ICN", "A"]

    result = solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"]])
    print(f'result = {result}')
    assert result == ["ICN", "A", "ICN", "A"]

