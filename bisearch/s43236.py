# -*- coding: utf-8 -*-
'''
징검다리 : https://programmers.co.kr/learn/courses/30/lessons/43236
'''


def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.insert(0, 0)
    rocks.sort()

    low, high = 1, distance
    answer = distance
    while low <= high:
        intervals = []
        for i in range(len(rocks) - 1):
            intervals.append(rocks[i+1] - rocks[i])
        mid = (low + high) // 2
        cnt = 0
        temp = float('inf')
        for i in range(len(intervals)):
            if intervals[i] < mid:
                cnt += 1
                if i < len(intervals) - 1:
                    intervals[i + 1] = intervals[i + 1] + intervals[i]
            else:
                temp = min(temp, intervals[i])

        if cnt > n:
            high = mid - 1
        else:
            answer = temp
            low = mid + 1

    return answer


if __name__ == '__main__':
    result = solution(25, [2, 14, 11, 21, 17], 2)
    print(result)
    assert result == 4

    # # 25 _ [2, 14, 11, 21, 17, 24] _ 3
    # assert solution(25, [2, 14, 11, 21, 17, 24], 3) == 4
    result = solution(25, [2, 6, 10], 3)
    print(result)
    assert result == 25