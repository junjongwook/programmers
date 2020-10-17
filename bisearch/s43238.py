# -*- coding: utf-8 -*-
'''
입국심사 : https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
'''

def solution(n, times):
    answer = 0
    lastTime = [0] * len(times)
    for i in range(n):
        _lastTime = [lastTime[j] + times[j] for j in range(len(times))]
        answer = min(_lastTime)
        index = _lastTime.index(answer)
        lastTime[index] = answer

    return answer


if __name__ == '__main__':
    result = solution(6, [7, 10])
    print(result)
    assert result == 28

