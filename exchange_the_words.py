n = input()
m = list(n.split())[-1::-1]
a = []
for i in m:
    a.append(i)
print(*a)