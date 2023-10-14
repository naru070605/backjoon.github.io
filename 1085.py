x, y, w, h = map(int, input().split())
m = [x,y, (w-x), (h-y)]
p = 10000
for i in range(4):
    if p > m[i]:
        p = m[i]
print(p)