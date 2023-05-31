n = input()
l = []
a = ("a","e","i","o","u")
for i in n:
    if i not in l and i in a:
        l.append(i)
if len(l) == 5:
    print("0")
    
else:
    for i in a:
        if i not in l:
            print(i , end = ' ')