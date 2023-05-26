n = int(input())
arr = list(map(int,input().split()))
a = []
b = []
for i in arr:
    if i % 2 != 0:
        a.append(i)
    else:
        b.append(i)
c=b+a
print(*c)