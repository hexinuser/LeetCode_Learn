# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:10:40 2019

@author: Evan_He
"""
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while True:
            if n <= 9*10**k*(k+1):
                t = 10**k +(n-1)//(k+1)
                mod = n%(k+1)
                if mod == 0:
                    return t%10
                else:
                    #return int(str(t)[mod-1])
                    return t//(10**(k+1-mod))%10
            n -= 9*10**k*(k+1)
            k += 1