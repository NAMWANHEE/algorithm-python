# 나무 자르기 문제와 동일한 문제로 결과 도출과정만 살짝 바뀐 문제
a, b = map(int,input().split())
li = [int(input()) for _ in range(a)]
start = 1
end = max(li)
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in li:
        cnt += i//mid
        if cnt >=b:
            break
    if cnt >= b:
        start = mid+1
    else:
        end = mid-1
print(end)