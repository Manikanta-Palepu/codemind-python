n = int(input())
lst = list(map(int,input().split()))
fh = 0
sh = 0
for i in range(0 , n//2):
    fh += lst[i]
for i in range(n//2 , n):
    sh += lst[i]
print(fh)
print(sh)