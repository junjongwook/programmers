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
            heapq.heappush(heap, (end, job))
        start, _job = heapq.heappop(heap)
        jobs.remove(_job)
        temp.append((start, _job))

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