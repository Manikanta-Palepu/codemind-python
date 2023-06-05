n = int(input())
lst = list(map(int,input().split()))
a = 0
for i in range(0 , n):
    if lst[i]%2!=0:
        break
    a += lst[i]
print(a)    