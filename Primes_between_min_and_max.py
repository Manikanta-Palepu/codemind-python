n = int(input())
l = list(map(int,input().split()))
c = 0
a = l.index(min(l))
b = l.index(max(l))
if a>b:
    a,b = b,a
for i in range(a , b+1):
    f = 0
    for j in range(2 , l[i]):
        if l[i] % j == 0:
            f += 1
    if l[i] > 1 and l[i] != 0 and f == 0:
        c += 1
print(c)