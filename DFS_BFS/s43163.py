# -*- coding: utf-8 -*-
'''
단어 변환 : https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
'''


def solution(begin, target, words):
    res = []
    visited = [0] * len(words)

    def count(word1, word2):
        _count = 0
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                _count += 1

        return _count

    def dfs(word, depth):
        if word == target:
            res.append(depth)
            return
        else:
            for i in range(len(words)):
                if visited[i] == 1:
                    continue

                if count(word, words[i]) == 1:
                    visited[i] = 1
                    dfs(words[i], depth + 1)
                    visited[i] = 0

    dfs(begin, 0)
    if len(res) > 0:
        return min(res)
    else:
        return 0


if __name__ == '__main__':
    result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print(f'result = {result}')
    assert result == 4

    result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print(f'result = {result}')
    assert result == 0


