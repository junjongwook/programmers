# -*- coding: utf-8 -*-
'''
트리 트리오 중간값 : https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
'''


def solution(n, edges):
    answer = 0
    edgeDict = dict()
    for v1, v2 in edges:
        edgeDict.setdefault(v1, [])
        edgeDict.setdefault(v2, [])
        edgeDict[v1].append(v2)
        edgeDict[v2].append(v1)

    def 제일_먼곳_찾기(시작):
        '''
        제일 먼곳을 찾는데 결과는 여러개 일 수 있음
        :param 시작: 시작위치
        :return: [(위치, 거리)]
        '''
        방문여부 = [0] * ( n + 1)
        stack = [(시작, 0)]
        결과 = []
        max거리 = 0
        while stack:
            위치, 거리 = stack.pop()
            방문여부[위치] = 1
            if 거리 > max거리:
                max거리 = 거리
                결과 = [(위치, 거리)]
            else:
                결과.append((위치, 거리))
            for 다음위치 in edgeDict[위치]:
                if 방문여부[다음위치] == 0: # 방문한 곳이 아니면
                    stack.append((다음위치, 거리 + 1))
        return 결과
            
    # 첫번째 노드에서 제일 먼 곳의 노드를 하나 찾는다.
    트리지름_위치들 = 제일_먼곳_찾기(edges[0][0])

    # 트리지름의 끝점들을 대상으로 다른 대상의 끝점을 찾아본다.
    for 트리지름_위치1, _거리 in 트리지름_위치들:
        임시결과 = 제일_먼곳_찾기(트리지름_위치1)
        if len(임시결과) > 1:
            answer = 임시결과[0][1]
            break
        else:
            answer = 임시결과[0][1] - 1

    return answer


if __name__ == '__main__':
    result = solution(4, [[1,2],[2,3],[3,4]])
    print(f'result = {result}')
    assert result == 2

    result = solution(5, [[1,5],[2,5],[3,5],[4,5]]	)
    print(f'result = {result}')
    assert result == 2

