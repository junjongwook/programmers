# -*- coding: utf-8 -*-
"""
자물쇠와 열쇠 : https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""


def solution(key, lock):
    lock_width = len(lock)
    key_width = len(key)

    def match(start_h, start_w):
        for h in range(start_h, min(lock_width, start_h + key_width)):
            for w in range(start_w, min(lock_width, start_w + key_width)):
                key_h = h - start_h
                key_w = w - start_w
                if key[key_h][key_w] == lock[h][w]:
                    return False

        return True

    for i in range(4):  # 3번만 시계방향으로 돌려보면 된다.
        for start_h in range(lock_width):
            for start_w in range(lock_width):
                answer = match(start_h, start_w)
                if answer:
                    return True
        key = list(map(list, zip(*key[::-1])))

    return False


if __name__ == '__main__':
    result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(f'result = {result}')
    assert result == True
