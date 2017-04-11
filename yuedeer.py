a = []
samenum = 0
l = input()
llist = list(l)
for x in llist:
    if x.isalnum():
        a.append('1')
    else:
        a.append('0')
xk = list(input())
for x in range(len(llist)):
    if a[x] == xk[x]:
        samenum += 1
    else:
        continue
print(a)
print(xk)
percent = float(samenum)/float(len(llist))*100
print('%.2f%%' %percent)