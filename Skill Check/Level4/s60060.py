# -*- coding: utf-8 -*-
"""
가사 검색 : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()

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

    def isLeaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def __str__(self, level=0):
        temp = '\t' * level + repr(self.value) + '\n'
        for child in self.children.values():
            temp += child.__str__(level + 1)
        return temp

root = Node('')     # 정방향으로 확인할 경우의 root
tail = Node('')     # 역방향에서 확인할 경우의 root

def makeTree(w):
    curr = root
    for c in w:
        if not curr.hasChildCharacter(c):
            curr.setChildNode(c)
        curr = curr.getChildNode(c)

def makeReverseTree(w):
    curr = tail
    index = len(w)
    for i in range(index - 1, -1, -1):
        if not curr.hasChildCharacter(w[i]):
            curr.setChildNode(w[i])
        curr = curr.getChildNode(w[i])


def search(query):
    if query[0] == '?':
        return searchBackward(query)
    else:
        return searchForward(query)

def searchForward(query):
    answer = 0
    width = len(query)
    stack = [root]
    for i in range(width - 1):
        _stack = []
        while stack:
            node = stack.pop()
            if query[i] == '?':
                _stack.extend(node.getChildren())
            elif node.hasChildCharacter(query[i]):
                _stack.append(node.getChildNode(query[i]))
        stack = _stack
    # 마지막은 항상 '?' 이므로
    for s in stack:
        children = s.getChildren()
        for child in children:
            if child.isLeaf():
                answer += 1

    return answer


def searchBackward(query):
    answer = 0
    width = len(query)
    stack = [tail]
    for i in range(width - 1, 0, -1):
        _stack = []
        while stack:
            node = stack.pop()
            if query[i] == '?':
                _stack.extend(node.getChildren())
            elif node.hasChildCharacter(query[i]):
                _stack.append(node.getChildNode(query[i]))
        stack = _stack
    # 마지막은 항상 '?' 이므로
    for s in stack:
        children = s.getChildren()
        for child in children:
            if child.isLeaf():
                answer += 1

    return answer

def solution(words, queries):
    answer = []

    for word in words:
        makeTree(word)
        makeReverseTree(word)

    # print(root)
    # print(tail)
    #
    # print(searchForward('fro??'))
    # print(searchBackward('????o'))
    for query in queries:
        answer.append(search(query))

    return answer


if __name__ == '__main__':
    result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
    print(f'result = {result}')
    assert result == [3, 2, 4, 1, 0]