# -*- coding: utf-8 -*-
"""
자물쇠와 열쇠 : https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""


def solution(key, lock):
    lock_width = len(lock)
    key_width = len(key)

    def key_value(start_h, start_w, h, w):
        _h = h - start_h
        _w = w - start_w
        if 0 <= _h < key_width and 0 <= _w < key_width:
            return key[_h][_w]

        return None

    for i in range(4):  # 3번만 시계방향으로 돌려보면 된다.
        # key block 의 시작위치를 설정한다.
        for start_key_h in range(-key_width + 1, lock_width):
            for start_key_w in range(-key_width + 1, lock_width):
                answer = True   # Loop 를 성공적으로 돌면 True 를 반환할 예정이다.
                # lock 블록은 모두 체크한다.
                for h in range(lock_width):
                    for w in range(lock_width):
                        value = key_value(start_key_h, start_key_w, h, w)
                        if value == None and lock[h][w] == 0:
                            answer = False
                            break
                        if value == lock[h][w]: # 같은 돌기이거나 홈이면
                            answer = False
                            break
                    if not answer:
                        break
                if answer:  # lock 블록을 무사히 마치면
                    return True

        key = list(map(list, zip(*key[::-1])))

    return False


if __name__ == '__main__':
    result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(f'result = {result}')
    assert result == True
