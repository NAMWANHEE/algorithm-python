from collections import deque
n,w,l = map(int,input().split())
truck = deque(map(int,input().split()))
br = deque([0 for _ in range(w)])
count = 0
weight = 0
while True:

    out = br.popleft()
    weight -= out
    count += 1
    if truck:
        if weight + truck[0] <= l:
            weight += truck[0]
            br.append(truck.popleft())
        else:
            br.append(0)


    if not br:
        break


print(count)