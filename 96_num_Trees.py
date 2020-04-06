# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:13:31 2019

@author: Evan_He
"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        S_i = [1,1,2]
        i = 3
        res = 0
        while i <= n:
            for k in range(i//2):
                res += (S_i[k]*S_i[i-k-1])*2
            if i % 2 == 1:
                res += S_i[k+1]**2
            S_i.append(res)
            res = 0
            i += 1
        return S_i[-1]
"""
class Solution:
    def numTrees(self, n):

        sum_1 = 1
        for i in range (n+1,2*n+1):
            sum_1 *= i

        sum_2 = 1
        for i in range(1,n+1):
            sum_2 *= i

        return int((sum_1/sum_2)/(n+1))
"""