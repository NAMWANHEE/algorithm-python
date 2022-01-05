answer = [] # 초반에는 9명 난쟁이 모두 담고 나중엔 정답인 7난쟁이들만 담을 리스트
for i in range(9):  #9명 난쟁이의 키 입력
    answer.append(int(input()))

total = sum(answer) # 총 9난쟁이의 키를 더한값 -> 9명의 합에서 2명의 키를 뺐을때 100이되면 정답
for i in range(0,len(answer)-1): # 모든 경우를 다돌면서 2명의 키의 합을 뺐을때 100이되면 반복문 종료
    for j in range(1,len(answer)):
        if total - (answer[i]+answer[j]) == 100:
            de1 = answer[i]
            de2 = answer[j]
            answer.remove(de1)
            answer.remove(de2)
            break # 난쟁이의 수가 7명이 되면 반복문 종료
    if len(answer) == 7:
        break
for i in sorted(answer): # 정렬하여 7난쟁이의 키를 출력
    print(i)

