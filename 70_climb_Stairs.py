# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:16:16 2018

@author: Evan_He
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            count = 0
            for i in range(1,3):
                count += self.climbStairs(n-i)
            return count
        """
        
        if n == 0:
            return 1
        if n == 1:
            return 1
        a0 =1 
        a1 =1
        k=2
        while k<=n:
            result = a0+a1
            a0, a1 = a1,result
            k+=1
        return result
        """
        def out(n,k):
            result = 1
            for i in range(1,k+1):
                result *= (n-i+1)/i
            return int(result)
        t = int(n/2)
        count = 0
        for j in range(t+1):
            count += out(n-j,j)
        return count
        """
    