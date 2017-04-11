# -*- coding:utf-8 -*-
class GoUpstairs:

    def countWays(self, n):
        a = [0]*100000
        a[0]=1
        a[1]=2
        a[2]=4
        for x in range(3,n):
            a[x]=a[x-1]+a[x-2]+a[x-3]
        return a[n-1]

A = GoUpstairs()
print(A.countWays(4))