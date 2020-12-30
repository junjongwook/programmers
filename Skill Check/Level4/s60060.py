# -*- coding: utf-8 -*-
"""
가사 검색 : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.childrenCount = 0

    def hasChildCharacter(self, c):
        if c in self.children:
            return True
        else:
            return False

    def getChildNode(self, c):
        if self.hasChildCharacter(c):
            return self.children[c]
        else:
            return None

    def getChildren(self):
        return list(self.children.values())

    def setChildNode(self, c):
        self.children[c] = Node(c)

    def __str__(self, level=0):
        temp = '\t' * level + f'value: {self.value}, childrenCount = {self.childrenCount}' + '\n'
        for child in self.children.values():
            temp += child.__str__(level + 1)
        return temp


dictionary = dict()             # 정방향 사전
dictionary2 = dict()            # 역방향 사전


def makeTree(w, width):
    dictionary.setdefault(width, Node(''))
    curr = dictionary.get(width)
    for c in w:
        curr.childrenCount += 1
        if not curr.hasChildCharacter(c):
            curr.setChildNode(c)
        curr = curr.getChildNode(c)

def makeReverseTree(w, width):
    dictionary2.setdefault(width, Node(''))
    curr = dictionary2.get(width)
    index = len(w)
    for i in range(index - 1, -1, -1):
        curr.childrenCount += 1
        if not curr.hasChildCharacter(w[i]):
            curr.setChildNode(w[i])
        curr = curr.getChildNode(w[i])

def search(query):
    width = len(query)
    if query[0] == '?':
        return searchBackward(query, width)
    else:
        return searchForward(query, width)

def searchForward(query, width):
    answer = 0
    if width not in dictionary:
        return 0
    curr = dictionary.get(width)
    for i in range(width):
        if query[i] == '?':
            answer = curr.childrenCount
            break
        if curr.hasChildCharacter(query[i]):
            curr = curr.getChildNode(query[i])

    return answer


def searchBackward(query, width):
    answer = 0
    if width not in dictionary2:
        return 0
    curr = dictionary2.get(width)
    for i in range(width - 1, 0, -1):
        if query[i] == '?':
            answer = curr.childrenCount
            break
        if curr.hasChildCharacter(query[i]):
            curr = curr.getChildNode(query[i])

    return answer


def solution(words, queries):
    answer = []

    for word in words:
        makeTree(word, len(word))
        makeReverseTree(word, len(word))

    # print(f'dictionary = {repr(dictionary)}')
    # print(searchForward('fro??'))
    # print(searchBackward('????o'))
    for query in queries:
        answer.append(search(query))

    return answer


if __name__ == '__main__':
    result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
    print(f'result = {result}')
    assert result == [3, 2, 4, 1, 0]