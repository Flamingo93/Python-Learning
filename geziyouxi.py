n,m = input().strip().split()
i=0
j=0
l=[]
c=[]
while i<int(n):
    l.append(int(input()))
    i += 1
# print(l)
while j<int(m):
    c.append(list(map(int, list(input().strip().split()))))
    j += 1
# print(c)
for x in range(len(c)):
    if c[x][0] == 1:
        pass
    if c[x][0] == 2:
        s = 0
        print(sum(l[c[x][1]-1:c[x][2]]))
    if c[x][0] == 3:
        print(max(l[c[x][1]-1:c[x][2]]))