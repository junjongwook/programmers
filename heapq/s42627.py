# -*- coding: utf-8 -*-
'''
디스크 컨트롤러
'''

def solution(jobs):
    answer = 0

    import heapq
    start = 0
    temp = []
    while jobs:
        heap = []
        for job in jobs:
            end = max(start, job[0]) + job[1]
            heapq.heappush(heap, (max(start, job[0]), end, job))
        _start, _end, _job = heapq.heappop(heap)
        jobs.remove(_job)
        temp.append((_end, _job))
        start = _end

    _sum = 0
    for t in temp:
        end, [start, end2] = t
        _sum += (end - start)

    answer = int(_sum / len(temp))

    return answer


if __name__ == '__main__':
    result = solution([[0, 3], [1, 9], [2, 6]])
    print(result)
    assert result == 9

    assert solution([[0, 3], [4, 3], [10, 3]] ) == 3
    assert solution([[0, 10], [2, 3], [9, 3]]) == 9
    assert solution([[1, 10], [3, 3], [10, 3]] ) == 9
    assert solution([[0, 10]] ) == 10
    assert solution([[0, 10], [4, 10], [5, 11], [15, 2]]) == 15
    assert solution([[0, 1], [1, 2], [500, 6]]) == 3
    assert solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]) == 13
    assert solution([[0, 5], [1, 2], [5, 5]]) == 6