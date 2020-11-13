# -*- coding: utf-8 -*-
'''
[1차]다트게임
'''


def solution(dartResult):
    answer = 0
    points = [0]
    import re
    p = re.compile('\d{1,2}[SDT][#\*]?')
    p2 = re.compile('\d{1,2}')
    p3 = re.compile('[SDT]')
    p4 = re.compile('[#\*]')
    darts = p.findall(dartResult)
    for dart in darts:
        _point = p2.match(dart)
        point = int(_point.group())
        _power = p3.search(dart)
        power = _power.group()
        if power == 'S':
            pass
        elif power == 'D':
            point = point ** 2
        elif power == 'T':
            point = point ** 3
        _option = p4.search(dart)
        if _option is None:
            points.append(point)
        else:
            option = _option.group()
            if option == '*':
                points[-1] = points[-1] * 2
                points.append(point * 2)
            elif option == '#':
                points.append(-point)

    answer = sum(points)

    return answer


if __name__ == '__main__':
    result = solution("1S2D*3T")
    print(f'result = {result}')
    assert result == 37

