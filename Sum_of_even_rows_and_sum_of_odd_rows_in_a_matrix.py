r , c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
e = 0
o = 0
for i in range(r):
    for j in range(c):
        if i%2==0:
            e += arr[i][j]
        else:
            o += arr[i][j]
print(e,o)