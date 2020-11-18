# -*- coding: utf-8 -*-
"""
[3차]방금그곡 : https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3
"""

def change(m):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    return m

def solution(m, musicinfos):
    answer = '(None)'
    m = change(m)

    class MusicInfo:
        def __init__(self, data):
            self.start, self.end, self.title, self.music = data.split(',')
            self.music = change(self.music)

        def match(self, m):
            temp = self.music
            while len(temp) < self.elapsed():
                temp += self.music
            temp = temp[:self.elapsed()]

            return m in temp

        def elapsed(self):
            '''
            연주되는 음의 개수
            :return: 음의 개수
            '''
            _start = int(self.start[0:2]) * 60 + int(self.start[3:5])
            _end = int(self.end[0:2]) * 60 + int(self.end[3:5])
            return _end - _start

    _match = None
    for musicinfo in musicinfos:
        _m = MusicInfo(musicinfo)
        if _m.match(m):
            if _match is None:
                _match = _m
                answer = _m.title
            elif _match.elapsed() < _m.elapsed():
                _match = _m
                answer = _m.title

    return answer


if __name__ == '__main__':
    # result = solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
    # print(f'result = {result}')
    # assert result == "HELLO"
    #
    # result = solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
    # print(f'result = {result}')
    # assert result == "WORLD"

    result = solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
    print(f'result = {result}')
    assert result == "FOO"

    result = solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"])
    print(f'result = {result}')