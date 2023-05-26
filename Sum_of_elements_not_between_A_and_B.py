n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
c = []
for i in arr:
    if i<a or i>b:
        c.append(i)
print(sum(c))