n = input()
v = []
count = 0
for i in range(len(n)):
    if (n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u') or (n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U'):
        if n[i] not in v:
            print(n[i] , end = ' ')
        v.append(n[i])
        count += 1
if count == 0:
    print('-1')