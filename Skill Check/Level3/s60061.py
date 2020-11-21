# -*- coding: utf-8 -*-
"""
기둥과 보 설치 : https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3
"""


def solution(n, build_frame):
    answer = []
    bo_frame = [[None] * (n+1) for _ in range(n+1)]
    gi_frame = [[None] * (n+1) for _ in range(n+1)]


    def isOk():
        for h in range(n+1):
            for w in range(n+1):
                if not gi_frame[h][w] is None:  # 기둥이 있다면 유효한지 확인
                    if h == 0:  # 바닥에 놓인 거라면 통과
                        pass
                    elif not gi_frame[h-1][w] is None:  # 아래에 기둥이 있으면 통과
                        pass
                    elif w > 0 and (not bo_frame[h][w-1] is None):  # 좌측에 보가 있으면 통과
                        pass
                    elif not bo_frame[h][w] is None:    # 보가 있다면 통과
                        pass
                    else:   # 이런 조건이 안 맞다면 실패
                        return False

                if not bo_frame[h][w] is None:  # 보가 있다면 유효한지 확인
                    if h == 0:  # 바닥이라면 통과
                        pass
                    elif not gi_frame[h-1][w] is None:  # 왼쪽 아래에 기둥이 있다면
                        pass
                    elif w < n and (not gi_frame[h-1][w+1] is None): # 오른쪽 아래에 기둥이 있다면
                        pass
                    elif (0 < w < n) and (not bo_frame[h][w-1] is None) and (not bo_frame[h][w+1] is None):  # 왼쪽에 보가 있다면
                        pass
                    else:
                        return False
        return True


    for frame in build_frame:
        _w, _h, _gb, _bd = frame
        if _gb == 0:    # 기둥일때
            if _bd == 0:    # 삭제일때
                if gi_frame[_h][_w] is None:
                    pass
                else:
                    gi_frame[_h][_w] = None
                    if isOk():
                        pass
                    else:
                        gi_frame[_h][_w] = 0
            elif _bd == 1: #추가일때
                if gi_frame[_h][_w] is None:
                    gi_frame[_h][_w] = 0
                    if isOk():
                        pass
                    else:
                        gi_frame[_h][_w] = None
                else:
                    pass
        elif _gb == 1:  # 보일때
            if _bd == 0:    # 삭제일때
                if bo_frame[_h][_w] is None:
                    pass
                else:
                    bo_frame[_h][_w] = None
                    if isOk():
                        pass
                    else:
                        bo_frame[_h][_w] = 1
            else:   # 추가일 때
                if bo_frame[_h][_w] is None:
                    bo_frame[_h][_w] = 1
                    if isOk():
                        pass
                    else:
                        bo_frame[_h][_w] = None
                else:
                    pass

    # 정보 추출
    for h in range(n+1):
        for w in range(n+1):
            if not gi_frame[h][w] is None:
                answer.append([w, h, gi_frame[h][w]])
            if not bo_frame[h][w] is None:
                answer.append([w, h, bo_frame[h][w]])

    # 정렬하기
    answer.sort()

    return answer


if __name__ == '__main__':
    # result = solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
    # print(f'result = {result}')
    # assert result == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]

    result = solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
    print(f'result = {result}')
    assert result == 	[[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
