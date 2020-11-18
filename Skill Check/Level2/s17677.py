# -*- coding: utf-8 -*-
"""
[1차]뉴스 클러스터링
"""

def get다중집합(str):
    d = dict()
    for i in range(len(str) - 1):
        if str[i].isalpha() and str[i+1].isalpha():
            datum = str[i:i+2]
            datum = datum.lower()
            d.setdefault(datum, 0)
            d[datum] += 1

    return d


def solution(str1, str2):
    d1 = get다중집합(str1)
    d2 = get다중집합(str2)

    if len(d1) == 0 and len(d2) == 0: return 65536

    교집합 = 0
    합집합 = 0
    for k, v in d1.items():
        if k in d2:
            교집합 += min(v, d2[k])
            합집합 += max(v, d2[k])
        else:
            합집합 += v
            
    for k, v in d2.items():
        if k in d1:
            pass
        else:
            합집합 = 합집합 + v
            
    return int(65536 * 교집합 / 합집합)


if __name__ == '__main__':
    result = solution("FRANCE", "french")
    print(f'result = {result}')
    assert result == 16384

    result = solution("E=M*C^2", "E=M*C^2")
    print(f'result = {result}')
    assert result == 65536

    result = solution("aa1+aa2", "AAAA12")
    print(f'result = {result}')
    assert result == 43690

    result = solution("handshake", "shake hands")
    print(f'result = {result}')
    assert result == 65536


