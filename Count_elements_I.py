n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
for i in a:
    if i in b:
        l.append(i)
for j in b:
    if j in a:
        l.append(j)
x = set(l)
print(len(x))