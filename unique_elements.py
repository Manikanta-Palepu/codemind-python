a=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(len(l)):
    if l[i] not in x:
        x.append(l[i])
print(*x)