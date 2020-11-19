# -*- coding: utf-8 -*-
"""
자물쇠와 열쇠 : https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""

def rotate(arr2, direction=1):
    '''
    direction 이 1이면 시계방향으로 90도, -1 이면 반시계 방향으로 90도
    '''
    width = len(arr2[0])
    height = len(arr2)
    result = [[0] * height for _ in range(width)]
    for _h in range(height):
        for _w in range(width):
            if direction == -1:
                result[width - _w - 1][_h] = arr2[_h][_w]
            else:
                result[_w][height - _h - 1] = arr2[_h][_w]

    return result


def solution(key, lock):
    answer = True
    lock_width = len(lock)
    key_width = len(key)

    for i in range(3):  # 3번만 시계방향으로 돌려보면 된다.
        for start_h in range(lock_width):
            for start_w in range(lock_width):
                answer = True    # 성공여부
                for _h in range(start_h, min(lock_width, start_h + key_width)):
                    for _w in range(start_w, min(lock_width, start_w + key_width)):
                        key_h = _h - start_h
                        key_w = _w - start_w
                        if key[key_h][key_w] == lock[_h][_w]:
                            answer = False
                            break
                    if not answer:
                        break
                if answer:
                    break
            if answer:
                break
        if answer:
            break
        key = rotate(key, 1)

    return answer


if __name__ == '__main__':
    result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(f'result = {result}')
    assert result == True
