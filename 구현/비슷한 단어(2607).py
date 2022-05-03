import copy
n = int(input())
word = list(input()) # 맨 처음 단어
ans = 0
for i in range(n-1): # n-1 번 만큼 반복
    w = list(input()) # 단어 입력 (비교할 단어)
    word2 = copy.deepcopy(word) # 맨 처음 단어를 복사
    if abs(len(word) - len(w)) >= 2: # 혹시 두 단어의 개수 차이가 2 이상일때는 무조건 비슷한 단어가 아니므로 continue
        continue
    for _ in range(len(word2)): # 첫 단어의 길이만큼 반복
        a = word2.pop(0)        # a : 첫 단어의 가장 왼쪽 문자
        if a in w:              # 문자가 비교할 단어에 있다면
            w.remove(a)         # 해당 문자를 비교할 단어에서 삭제
        else:
            word2.append(a)     # 문자가 비교할 단어에 없다면 첫 단어에서 pop 하였으므로 다시 추가

    n1 = len(word2) # 첫 단어의 길이
    n2 = len(w)     # 비교할 단어의 길이
    if (n1 == 1 and n2 == 1) or (n1 == 1 and n2 == 0) or (n1 == 0 and n2 == 1) or (n1 == 0 and n2 == 0):
        ans += 1    # 단어의 길이가 각각 (1,1)or(1,0)or(0,1)or(0,0) 일 경우에만 비슷한 단어가 성립하므로 정답 카운트
print(ans)