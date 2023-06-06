n = input()
a = []
for i in n:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a.append(i)
print(len(a))