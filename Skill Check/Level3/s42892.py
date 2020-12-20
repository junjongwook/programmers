# -*- coding: utf-8 -*-
"""
길 찾기 게임 : https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3
"""

import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = [[], []]
    width = len(nodeinfo)

    class Node:
        def __init__(self, info, num):
            self.info = info
            self.x = info[0]
            self.y = info[1]
            self.num = num
            self.parent = None
            self.left = None
            self.right = None

        def __repr__(self):
            repr = 'info = ' + str(self.info) + ', '
            repr += 'num = ' + str(self.num) + ', '
            # repr += 'parent = ' + ('None' if self.parent is None else str(self.parent.info)) + ', '
            # repr += 'left = ' + ('None' if self.left is None else str(self.left.info)) + ', '
            # repr += 'right = ' + ('None' if self.right is None else str(self.right.info))
            return repr

        def __str__(self, level=0):
            _str = '\t' * (level * 5) + f'[info = {self.info}, num = {self.num}]'
            if self.left != None:
                _str += '\n' + self.left.__str__(level+1)
            if self.right != None:
                _str += '\n' + self.right.__str__(level+1)

            return _str

    treeList = []
    for i, coord in enumerate(nodeinfo, 1):
        node = Node(coord, i)
        treeList.append(node)

    treeList.sort(key=lambda node: node.info[0])
    
    def makeTree(treeList, start, end):
        '''
        구간에서 최고 높은 Node 를 찾아 낸다
        '''
        maxY = -1
        root = None
        index = -1
        for i in range(start, end + 1):
            if treeList[i].info[1] > maxY:
                maxY = treeList[i].info[1]
                root = treeList[i]
                index = i
        if root != None:
            root.left = makeTree(treeList, start, index - 1)
            root.right = makeTree(treeList, index + 1, end)

        return root

    # Tree 구조 만들기
    root = makeTree(treeList, 0, width - 1)
    # print(root)

    # pre-order traversal
    stack = [root]
    while stack:
        _node = stack.pop()
        answer[0].append(_node.num)
        if _node.right != None:
            stack.append(_node.right)
        if _node.left != None:
            stack.append(_node.left)

    # post-order traversal
    stack = [root]
    while stack:
        _node = stack.pop()
        if type(_node) == Node:
            stack.append(_node.num)
            if _node.right != None:
                stack.append(_node.right)
            if _node.left != None:
                stack.append(_node.left)
        else:
            answer[1].append(_node)

    return answer


if __name__ == '__main__':
    result = solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)
    print(f'result = {result}')
    assert result == [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
