n = int(input())
li = sorted(list(map(int,input().split()))) # 이분탐색을 위해 정렬
m = int(input())
li2 = list(map(int,input().split()))
ans = []

def binary(i, start, end):  # i: 현재 카드의 숫자, start: 가장 왼쪽의 인덱스, end: 가장 오른쪽 인덱스
    mid = (start+end) // 2 # 중간인덱스(mid) = 가장왼쪽+가장오른쪽 인덱스를 2로 나눈 몫
    if start > end:     # 찾는 숫자가 없는 경우 0 추가
        ans.append(0)
    elif i == li[mid]:  # 찾는 숫자를 찾는 경우 1 추가
        ans.append(1)
    elif i > li[mid]:   # 가진 숫자가 중간 위치의 숫자보다 클 경우 가장 왼쪽 인덱스를 중간인덱스+1로 설정
        binary(i,mid+1,end)
    else:               # 가진 숫자가 중간 위치의 숫자보다 작을 경우 가장 오른쪽 인덱스를 중간인덱스-1로 설정
        binary(i,start,mid-1)

for i in li2:
    binary(i,0,len(li)-1)
print(*ans)