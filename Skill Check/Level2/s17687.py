# -*- coding: utf-8 -*-
"""
[3차]n진수 게임 : https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
"""

기호 = "0123456789ABCDEF"

def 진법변환(num, base):
    몫, 나머지 = divmod(num, base)
    return (진법변환(몫, base) + 기호[나머지]) if 몫 else 기호[나머지]


def solution(n, t, m, p):
   answer = ""
   currNumber = 0
   turn = 1
   if m == p: p = 0
   exitFlag = False
   while True:
        strNumber = 진법변환(currNumber, n)
        for s in list(strNumber):
            if turn % m == p:
               answer = answer + s
               if len(answer) == t:
                   exitFlag = True
                   break
            turn = turn + 1
        if exitFlag:
            break
        currNumber = currNumber + 1

   return answer


if __name__ == '__main__':
    result = solution(2, 4, 2, 1)
    print(f'result = {result}')
    assert result == "0111"

    result = solution(16, 16, 2, 1)
    print(f'result = {result}')
    assert result == "02468ACE11111111"