n = input()
m = n.split()
a = []
for i in m:
    a.append(len(i))
print(*a)