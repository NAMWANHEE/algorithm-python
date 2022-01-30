import heapq

n = int(input())
ans = []           # 최대값 n 개를 담을 리스트
for i in range(n):
    a = list(map(int,input().split()))
    for j in a:
        heapq.heappush(ans, j) # a 리스트에 있는 모든 값들을 ans 리스트에 담는다
        if len(ans) > n:       # 메모리 제한이 있어 ans의 길이가 n을 초과하면
            heapq.heappop(ans) # 리스트에서 가장 작은 값 pop

print(ans[0])                  # n번째로 큰 수를 출력하기 때문에 가장 첫번째 값 출력