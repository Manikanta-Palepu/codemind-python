n = input()
a = []
for i in n:
    if i in "abcdefghijklmnopqrstuvwxyz":
        a.append(i)
print(len(a))