n = int(input())
lst = list(map(int,input().split()))
k = int(input())
a = 0
for i in range(0 , k):
    a += lst[i]
print(a)