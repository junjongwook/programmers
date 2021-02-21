# -*- coding: utf-8 -*-
"""
신규 아이디 추천 : https://programmers.co.kr/learn/courses/30/lessons/72410
"""


def solution(new_id):
    import string
    available = string.ascii_lowercase + string.digits + "-" + "_" + "."
    PERIOD = '.'
    # 1단계 - 대문자를 모두 소문자로...
    new_id = new_id.lower()
    # 2단계 - 가능한 문자 외에는 모두 삭제
    temp = ''
    for c in new_id:
        if c in available:
            temp += c
    new_id = temp
    # 3단계 - period 가 2개 이상일 경우 하나로 줄임
    previous = ''
    temp = ''
    for c in new_id:
        if previous == PERIOD and c == PERIOD:
            pass
        else:
            temp += c
        previous = c
    new_id = temp
    # 4단계 - period 가 시작이나 끝에 있으면 삭제한다.
    if len(new_id) > 0 and new_id[0] == PERIOD:
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == PERIOD:
        new_id = new_id[:-1]
    # 5단계 - 빈 문자열일 경우 new_id 에 'a 를 대입한다.
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계 - 길이가 16자 이상이면.. 15자리로 하고, 끝이 . 이면 없앤다.
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == PERIOD:
            new_id = new_id[:-1]
    # 7단계 - 길이가 2자 이하라면 마지막 문자로 3일 될 때까지 만든다.
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


if __name__ == '__main__':
    result = solution("...!@BaT#*..y.abcdefghijklm")
    print(f'result = {result}')
    assert result == "bat.y.abcdefghi"

    result = solution("z-+.^.")
    print(f'result = {result}')
    assert result == "z--"

    result = solution("=.=")
    print(f'result = {result}')
    assert result == "aaa"

    result = solution("123_.def")
    print(f'result = {result}')
    assert result == "123_.def"

    result = solution("abcdefghijklmn.p")
    print(f'result = {result}')
    assert result == "abcdefghijklmn"