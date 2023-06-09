def pal(n):
    if n == n[::-1]:
        return True
    else:
        False
n = input()
k = n.split()
c = 0
for i in k:
    s = i.casefold()
    if (pal(s)):
        c += 1
print(c)