# -*- coding: utf-8 -*-
"""
가사 검색 : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
"""
from collections import defaultdict

def solution(words, queries):
    answer = []
    d = defaultdict(dict)      # startswith
    d2 = defaultdict(dict)     # endswith
    for word in words:
        width = len(word)
        for i in range(1, width):
            _start = word[:i]
            _last = width - i
            _end = word[-i:]
            _first = width - i
            if _last in d[_start]:
                d[_start][_last] += 1
            else:
                d[_start][_last] = 1
            if _first in d2[_end]:
                d2[_end][_first] += 1
            else:
                d2[_end][_first] = 1
    # print(f'd = {d}')
    # print(f'd2 = {d2}')

    for query in queries:
        width = len(query)
        if query[-1] == '?':
            index = width - query.count('?')
            start = query[:index]
            last = width - index
            if last in d[start]:
                answer.append(d[start][last])
            else:
                answer.append(0)
        elif query[0] == '?':
            index = query.count('?')
            end = query[index:]
            first = index
            if first in d2[end]:
                answer.append(d2[end][first])
            else:
                answer.append(0)

    return answer


if __name__ == '__main__':
    result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
    print(f'result = {result}')
    assert result == [3, 2, 4, 1, 0]