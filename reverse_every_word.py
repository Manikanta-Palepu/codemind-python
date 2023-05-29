def reverse(n):
    m = n.split()
    a = []
    for i in m:
        a.append(i[::-1])
    b = " ".join(a)
    return b
n = input()
print(reverse(n))