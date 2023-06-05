n = int(input())
lst = list(map(int,input().split()))
if len(lst) % 2 != 0:
    lst.extend('0')
print(*lst)