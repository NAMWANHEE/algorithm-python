for _ in range(10):
    n = int(input())
    arr = []
    ans = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    for i in arr:
        ans.append(sum(i))
    v1 = 0  # 대각선 1
    v2 = 0  # 대각선 2
    for i in range(100):
        v = 0
        for j in range(100):
            v += arr[j][i]
        ans.append(v)

        v1 += arr[i][i]
        v2 += arr[i][99 - i]
    ans.append(v1)
    ans.append(v2)

    print('#' + str(n), max(ans))