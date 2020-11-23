# -*- coding: utf-8 -*-
'''
여행경로 : https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
'''


def solution(tickets):
    answer = []
    티켓 = set()
    for ticket1, ticket2 in tickets:
        티켓.add(ticket1)
        티켓.add(ticket2)
    티켓 = list(티켓)
    티켓.sort()
    
    return answer


if __name__ == '__main__':
    result = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    print(f'result={result}')
    assert result == ["ICN", "JFK", "HND", "IAD"]

    result = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    print(f'result={result}')
    assert result == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
