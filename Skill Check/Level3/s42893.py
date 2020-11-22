# -*- coding: utf-8 -*-
"""
매칭 점수 : https://programmers.co.kr/learn/courses/30/lessons/42893?language=python3#
"""


import re

def solution(word, pages):

    class Page:
        def __init__(self, index, name, page, word):
            self.index = index
            self.name = name
            # 기본점수
            m = re.findall("[a-z]+", page.lower())
            self.basePoint = m.count(word.lower())

            # 외부 링크
            m = re.findall('<a href=[\"\'](\S+)[\"\']', page.lower())
            self.links = m

            self.linkPoint = 0

        def calcurate(self, pageDict):
            # 링크 점수
            for l in self.links:
                if l in pageDict:
                    pageDict[l].linkPoint += self.basePoint / len(self.links)

        def getMatchPoint(self):
            return self.basePoint + self.linkPoint


    pageDict = dict()
    for i, page in enumerate(pages):
        # page name
        m = re.search("<meta \S* content=[\"\'](\S+)[\"\']", page)
        name = m.group(1)
        pageDict[name] = Page(i, name, page, word)

    temp = []
    for name, page in pageDict.items():
        page.calcurate(pageDict)
        temp.append(page)

    temp.sort(key=lambda x: (-x.getMatchPoint(), x.index))
    answer = temp[0].index

    return answer


if __name__ == '__main__':
    result = solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    print(f'result = {result}')
    assert result == 0

    result = solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    print(f'result = {result}')
    assert result == 1
