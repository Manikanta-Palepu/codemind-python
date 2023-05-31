n = input()
count = 0
a = 'AEIOUaeiou'
for i in n:
    if i in a:
        count += 1
print(count)