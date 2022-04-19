n = int(input())
n_li = sorted(list(map(int,input().split())),reverse=True)
m = int(input())
m_li = sorted(list(map(int,input().split())),reverse=True)

ans = 0
if m_li[0] > n_li[0]:   # 가장 많은 무게를 드는 크레인보다 박스의 최대 무게가 더 크면 -1 출력
    print(-1)

else:
    while m_li:       # 박스가 담긴 리스트가 비어있을때까지 반복
        for i in n_li:      # i: 크레인이 들 수 있는 무게
            for j in m_li:  # j: 박스의 무게
                if i >= j:  # 크레인 무게가 박스의 무게보다 크면 해당 박스 삭제 후 이전 반복문으로 돌아가기
                    m_li.remove(j)
                    break


        ans += 1      # 크레인 무게에 대한 반복이 한번 끝날때 마다 정답 카운트 + 1
    print(ans)