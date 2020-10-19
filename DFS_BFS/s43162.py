# -*- coding: utf-8 -*-

def solution(n, computers):
    answer = 0
    visited = [None] * n

    stack = []
    for i, computer in enumerate(computers):
        if visited[i] == None:
            visited[i] = i
        else:
            continue

        stack.append(computer)
        while stack:
            temp = stack.pop()
            for j, t in enumerate(temp):
                if t == 0: continue
                if visited[j] != None:
                    continue
                visited[j] = i
                stack.append(computers[j])

    answer = len(set(visited))

    return answer


if __name__ == '__main__':
    result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(f'result = {result}')
    assert result == 2

    result = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    print(f'result = {result}')
    # assert result == 1
    
    result = solution(6, [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]])
    print(f'result = {result}')
    assert result == 1
