p = int(input())
t_list = list(map(int, input().split()))
t_list.sort(reverse=False)
s=0

for i in range(p):
    s += (p-i) * t_list[i]

print(s)
