from itertools import combinations

n = int(input())
s = list(map(int,input().split()))
a = []
for i in range(1,n+1):  # 조합할 수 있는 개수는 1부터 n까지 있다
    for j in list(combinations(s,i)): # 1개부터 n개 까지의 조합으로 나올 수 있는 모든 경우의수의 합을 a 에 추가
        a.append(sum(j))
num = 1 # 가장 작은 자연수인 1
ans = []
for i in sorted(list(set(a))): # 중복을 제거하고 정렬한 상태
    if num != i:             # num 과 i 가 같지 않다면
        ans.append(num)      # num 이 만들 수 없는 가장 작은 숫자 이므로 num 을 정답 리스트에 추가 후 break
        break
    num += 1                 # num 에 1 씩 더해줌

if len(ans) == 0:   # 정답이 담긴 리스트가 비어 있을 경우 (= 수열을 가지고 만들 수 있는 모든 값을 만들었다는 뜻)
    print(sum(s)+1) # 따라서 수열의 모든 값을 더한 후 거기에 + 1을 한 값이 만들 수 없는 가장 작은 수가 됨
else:
    print(ans[0])   # 정답리스트에 있는 값이 정답