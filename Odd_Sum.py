n = int(input())
arr = list(map(int,input().split()))
a = []
for i in arr:
    if i % 2 != 0:
        a.append(i)
print(sum(a))