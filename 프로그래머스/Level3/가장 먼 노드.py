from collections import deque


def solution(n, edge):
    answer = 0
    ans = [-1 for _ in range(n + 1)]  # 1번 노드로 부터 n번 노드까지의 거리
    info = [[] for _ in range(n + 1)]  # 각 노드로 부터 연결되어 있는 노드 정보 (인덱스 = 노드번호)
    for i in edge:  # 양방향 연결
        info[i[0]].append(i[1])
        info[i[1]].append(i[0])

    q = deque()
    q.append(1)  # 시작 노드(1)
    ans[1] = 0  # 1번 노드부터 1번 노드까지 거리는 0
    print(info)
    while q:  # bfs
        node = q.popleft()

        for i in info[node]:
            if ans[i] == -1:  # 최단 거리가 구해지지 않은 경우( =방문되지 않은 경우)
                ans[i] = ans[node] + 1  # 현재 최단 거리에 + 1
                q.append(i)  # 큐에 연결된 노드 추가

    maximum = max(ans)  # 1번 노드로 부터 가장 멀리 떨어진 노드의 거리
    for i in ans:
        if i == maximum:
            answer += 1  # 가장 멀리 떨어진 노드들 카운트
    return answer