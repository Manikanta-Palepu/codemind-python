r,c = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(r)]
a = []
for j in range(c):
    l=[]
    for k in range(r):
        l.append(mat[k][j])
    a.append(sum(l))
print(max(a))