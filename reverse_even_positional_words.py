n = input()
s = n.split()
l = []
for i in range(0 , len(s)):
    if i % 2 == 0:
        a = s[i][-1::-1]
        l.append(a)
    else:
        l.append(s[i])
print(*l)