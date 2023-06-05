n = int(input())
lst = list(map(int,input().split()))
m = []
n = []
for i in lst:
    if i % 2 != 0:
        m.append(i)
for j in m:
    if j not in n:
        n.append(j)
print(sum(n))