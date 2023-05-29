n = input()
m = n.split()
c = []
for i in m:
    c.append(len(i))
print(min(c))