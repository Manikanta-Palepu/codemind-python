n = int(input())
arr = list(map(int,input().split()))
average = sum(arr)/len(arr)
print('{:.2f}'.format(average))