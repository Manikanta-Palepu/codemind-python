n = int(input())
m = list(map(int,input().split()))
a = []
b = []
c = []
for i in m:
    if i%2!=0:
        a.append(i)
    else:
        b.append(i)
c = a + b
print(*c)