'''
크루스칼 알고리즘 - 그래프 내의 모든 정점을 가장 적은 비용으로 연결하는 알고리즘
=> 비용을 기준으로 오름차순으로 정렬 후 해당 간선을 방문 했는지 안했는지 (= 사이클이 만들어지는지 안만들어지는지) 확인해가며 풀어야하는 문제
'''

def solution(n, costs):
    costs.sort(key = lambda x:x[2])             # 비용이 낮은 순으로 정렬
    answer = costs[0][2]                        # 맨 처음 최소 비용
    nodes = set([costs[0][0],costs[0][1]])      # 비용이 가장 낮은 시작노드와 도착노드를 집합에 추가
    while len(nodes) != n:  # 집합의 길이가 n과 같으면 종료
        for i in range(1,len(costs)):
            if costs[i][0] in nodes and costs[i][1] in nodes: # 시작노드와 도착노드가 둘다 집합에 있는 경우 = 사이클이 존재하는 경우, 이미 최소비용경로가 존재
                continue                        # 따라서 continue
            if costs[i][0] in nodes or costs[i][1] in nodes:  # 시작노드 또는 도착노드가 집합에 존재하는 경우
                nodes.update([costs[i][0],costs[i][1]])       # 집합에 시작노드와 도착노드 모두 추가 (집합이라 중복 신경x)
                answer += costs[i][2]                  # 정답에 현재 비용 추가
                break
    return answer