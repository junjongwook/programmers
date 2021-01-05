# -*- coding: utf-8 -*-
"""
[3차] 자동완성 : https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.children = dict()

    def addChild(self, value):
        if value in self.children:
            self.children[value].count += 1
        else:
            self.children[value] = Node(value)

    def getChild(self, value):
        if value in self.children:
            return self.children[value]
        else:
            return None

    def __str__(self, level=0):
        temp = '\t' * level + f'value = {self.value}, count = {self.count}' + '\n'
        for child in self.children.values():
            temp += child.__str__(level+1)
        return temp


def solution(words):
    answer = 0

    root = Node('')

    # Trie 만들기
    for word in words:
        curr = root
        for w in word:
            curr.addChild(w)
            curr = curr.getChild(w)
    # print(root)

    def searchDepth(word):
        temp = 0
        curr = root
        for w in word:
            temp = temp + 1
            child = curr.getChild(w)
            if child.count == 1: return temp
            curr = child
        return temp

    for word in words:
        result = searchDepth(word)
        # print(f'word = {word}, result = {result}')
        answer += result

    return answer


if __name__ == '__main__':
    # result = solution(["go", "gone", "guild"])
    # print(f'result = {result}')
    # assert result == 7

    result = solution(["abc", "def", "ghi", "jklm"])
    print(f'result = {result}')
    assert result == 4

    # result = solution(["word", "war", "warrior", "world"])
    # print(f'result = {result}')
    # assert result == 15


