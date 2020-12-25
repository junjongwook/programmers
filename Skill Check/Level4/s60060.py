# -*- coding: utf-8 -*-
"""
가사 검색 : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
"""

def solution(words, queries):
    answer = []
    d = dict()      # startswith
    d2 = dict()     # endswith
    for word in words:
        width = len(word)
        for i in range(1, width):
            _start = word[:i]
            _last = width - i
            _end = word[-i:]
            _first = width - i
            d.setdefault(_start, [])
            d[_start].append(_last)
            d2.setdefault(_end, [])
            d2[_end].append(_first)
    # print(f'd = {d}')
    # print(f'd2 = {d2}')

    for query in queries:
        width = len(query)
        if query[-1] == '?':
            index = width - query.count('?')
            start = query[:index]
            last = width - index
            if start in d:
                answer.append(d[start].count(last))
            else:
                answer.append(0)
        elif query[0] == '?':
            index = query.count('?')
            end = query[index:]
            first = index
            if end in d2:
                answer.append(d2[end].count(first))
            else:
                answer.append(0)

    return answer


if __name__ == '__main__':
    result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
    print(f'result = {result}')
    assert result == [3, 2, 4, 1, 0]