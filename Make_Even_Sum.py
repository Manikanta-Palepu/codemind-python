n = int(input())
arr = map(int,input().split())
s = sum(arr)
if s % 2 == 0:
    print("1")
else:
    print("0")