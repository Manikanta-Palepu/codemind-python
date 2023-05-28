r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range (r)]
a = 0
for i in range (r):
    for j in range(c):
        a += arr[i][j]
print(a)