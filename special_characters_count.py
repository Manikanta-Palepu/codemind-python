n = input()
count = 0
for i in n:
    if i in '~!@#$%^&*()_+=-`{}][|;:"?><,./':
        count += 1
print(count)