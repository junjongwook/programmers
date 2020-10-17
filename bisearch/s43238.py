# -*- coding: utf-8 -*-
'''
입국심사 : https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
'''

def solution(n, times):
    answer = 0
    high = max(times) * n
    low = 0
    while low <= high:
        mid = int(high + low) // 2
        cnt = sum([mid // t for t in times])

        if cnt >= n:
            high = mid - 1
        else:
            low = mid + 1

    cnt = sum([low // t for t in times])
    if cnt >= n:
        answer = low
    else:
        answer = -1

    return answer


if __name__ == '__main__':
    result = solution(6, [7, 10])
    print(result)
    assert result == 28

