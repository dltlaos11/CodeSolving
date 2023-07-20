a,b = input().split()
c = ""
d = ""
for i in range(2, -1, -1):
    c = c + a[i]
    d = d + b[i]
if (int(c) > int(d)):
    print(c)
else:
    print(d)