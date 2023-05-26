n = int(input())
m = list(map(int,input().split()))
count = 0
average = sum(m)//len(m)
for i in m:
    if i>=average:
        count += 1
print(count)
        