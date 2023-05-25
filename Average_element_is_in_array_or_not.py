n = int(input())
arr = list(map(int,input().split()))
average = sum(arr)//len(arr)
if average in arr:
    print('True')
else:
    print('False')