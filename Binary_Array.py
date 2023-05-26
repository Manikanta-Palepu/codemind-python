n = int(input())
arr = list(map(int,input().split()))
a = []
for i in arr:
    if i==0 or i==1:
        a.append(i)
if len(arr)==len(a):
    print('True')
else:
    print('False')