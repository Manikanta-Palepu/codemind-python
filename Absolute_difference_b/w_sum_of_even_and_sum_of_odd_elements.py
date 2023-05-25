n = int(input())
arr = list(map(int,input().split()))
even = []
odd = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
se = sum(even)
so = sum(odd)
print(abs(se - so))