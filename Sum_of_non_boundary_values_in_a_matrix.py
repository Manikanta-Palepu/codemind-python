r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
s = 0
for i in range(r):
    for j in range(c):
        if i!=0 and j!=0 and i!=r-1 and j!=c-1:
            s += arr[i][j]
print(s)