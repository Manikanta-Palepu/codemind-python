n = int(input())
arr = list(map(int,input().split()))
fh = arr[:n//2]
sh = arr[n//2:]
print(abs(sum(fh) - sum(sh)))