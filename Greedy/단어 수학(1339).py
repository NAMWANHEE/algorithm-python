from collections import defaultdict
n = int(input())
li = []
dict = defaultdict(int)
for i in range(n):
    li.append(input())

for i in li:
    leng = len(i)           # 현재 단어의 길이
    for j in range(leng):
        dict[i[j]] += 10 ** (leng-j-1)  # 현재 단어의 문자의 자리에 맞게 사전에 갱신
ans = 0
num = 9
for i in sorted(dict.values(),reverse=True):    # 사전의 value를 기준으로 내림차순으로 정렬
    ans += num*i    # 가장 큰 값부터 9부터 -1 씩하며 곱해줌
    num -= 1
print(ans)