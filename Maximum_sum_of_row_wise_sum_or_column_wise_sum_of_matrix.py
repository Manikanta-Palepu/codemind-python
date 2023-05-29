r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
s = []
t = []
for i in range(r):
    k = 0
    for j in range(c):
        k += arr[i][j]
    s.append(k)
for i in range(r):
    l = 0
    for j in range(c):
        l += arr[i][j]
    t.append(l)
print(max(max(s),max(t)))