n = int(input())
lst = list(map(int,input().split()))
m = []
for i in lst:
    if i not in m:
        m.append(i)
print(sum(m))