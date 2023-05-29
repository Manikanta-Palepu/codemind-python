r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
s = 0
for i in range(r):
    for j in range(c):
        if i==j or i==c-j-1:
            s += arr[i][j]
print(s)