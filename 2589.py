a, b = map(int, input().split())
g = []
q = []
t = 0
for i in range(b):
    g.append(input().split())

def find(m,n,l,o):
    
    
    if i > 0:
        if g[i-1][j] == 'L':
            find()
    elif i < a-1:
        if g[i+1][j] == 'L':
            find()
    elif j > 0:
        if g[i][j-1] == 'L':
            find()
    elif j < b-1:
        if g[i][j+1] == 'L':
            find()

for i in range(a):
    for j in range(b):
        if g[i][j] == 'L':
            find(i,j,g,g)