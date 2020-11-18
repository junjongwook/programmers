# -*- coding: utf-8 -*-
"""
[3차]파일명 정렬 : https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3
"""


def solution(files):
    answer = []
    import re
    p = re.compile('([^\d]{0,})(\d{1,5}).*')

    def compare(x, y):
        m1 = p.search(x)
        h1, n1 = m1.group(1).lower(), int(m1.group(2))
        m2 = p.search(y)
        h2, n2 = m2.group(1).lower(), int(m2.group(2))

        if h1 < h2:
            return -1
        elif h1 == h2:
            return n1 - n2
        else:
            return 1

    from functools import cmp_to_key
    answer = sorted(files, key=cmp_to_key(compare))

    return answer


if __name__ == '__main__':
    # result = solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
    # print(f'result = {result}')
    # assert result == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

    result = solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
    print(f'result = {result}')
    assert result == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]