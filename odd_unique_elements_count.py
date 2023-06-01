n = int(input())
m = map(int,input().split())
l = []
for i in m:
    if i%2!=0 and i not in l:
        l.append(i)
print(len(l))