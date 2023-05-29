r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
s = 0
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:
            s += arr[i][j]
print(s)