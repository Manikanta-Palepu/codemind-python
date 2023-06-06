n , k = map(int,input().split())
l = list(map(int,input().split()))
count = 0
for i in l:
    a = str(i)
    b = len(a)
    if (i < 0):
        b -= 1
    if b == k:
        count += 1
print(count)