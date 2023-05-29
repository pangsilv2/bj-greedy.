N, K = map(int, input().split())
coin_ist = list()
for _ in range(N):
        coin_ist.append(int(input()))
ans = 0
for i in reversed(range(N)):
    ans += K//coin_ist[i]
    K = K%coin_ist[i]

print(ans)

