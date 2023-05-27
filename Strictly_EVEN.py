n = int(input())
lst = list(map(int,input().split()))
a = 0
for i in range(len(lst)):
    if lst[i]%2!=0 and i%2==0:
        a = 1
        break
if a == 0:
    print('True')
else:
    print('False')
        