# -*- coding: utf-8 -*-
"""
키패드 누르기 : https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
"""


def solution(numbers, hand):
    answer = ''
    leftButton = [1, 4, 7]
    rightButton = [3, 6, 9]
    centerButton = [2, 5, 8, 0]
    distance = dict()
    distance['*'] = [1, 3, 4, 5, 2, 3, 4, 1, 2, 3]
    distance['#'] = [1, 5, 4, 3, 4, 3, 2, 3, 2, 1]
    distance[0] = [0, 4, 3, 4, 3, 2, 3, 2, 1, 2]
    distance[1] = [4, 0, 1, 2, 1, 2, 3, 2, 3, 4]
    distance[2] = [3, 1, 0, 1, 2, 1, 2, 3, 2, 3]
    distance[3] = [4, 2, 1, 0, 3, 2, 1, 4, 3, 2]
    distance[4] = [3, 1, 2, 3, 0, 1, 2, 1, 2, 3]
    distance[5] = [2, 2, 1, 2, 1, 0, 1, 2, 1, 2]
    distance[6] = [3, 3, 2, 1, 2, 1, 0, 3, 2, 1]
    distance[7] = [2, 2, 3, 4, 1, 2, 3, 0, 1, 2]
    distance[8] = [1, 3, 2, 3, 2, 1, 2, 1, 0, 1]
    distance[9] = [2, 4, 3, 2, 3, 2, 1, 2, 1, 0]

    leftPosition = '*'
    rightPosition = '#'
    for n in numbers:
        if n in leftButton:
            answer += 'L'
            leftPosition = n
        elif n in rightButton:
            answer += 'R'
            rightPosition = n
        else:
            lDistance = distance[leftPosition][n]
            rDistance = distance[rightPosition][n]
            if lDistance < rDistance:
                answer += 'L'
                leftPosition = n
            elif lDistance > rDistance:
                answer += 'R'
                rightPosition = n
            else:
                if hand == 'left':
                    answer += 'L'
                    leftPosition = n
                else:
                    answer += 'R'
                    rightPosition = n

    return answer


if __name__ == '__main__':
    result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
    print(f'result = {result}')
    assert result == "LRLLLRLLRRL"

    result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')
    print(f'result = {result}')
    assert result == "LRLLRRLLLRR"

    result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')
    print(f'result = {result}')
    assert result == "LLRLLRLLRL"