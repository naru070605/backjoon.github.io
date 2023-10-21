a = []
c = 0
e = []
for i in range(10):
    b = int(input())
    a.append(b)
    if e.count(b) == 0:
        e.append(b)
    c += b
d = [0,0]
for i in e:
    f = a.count(i)
    if d[1] < f:
        d = [i,f]
print(c//10)
print(d[0])