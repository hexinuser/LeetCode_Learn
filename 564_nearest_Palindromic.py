# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:46:09 2019

@author: Evan_He
"""

class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        res = [i for i in n]
        length = len(res)
        k,m = length // 2, length % 2
        if res == res[::-1]:
            if m == 0:
                t= int(res[k])
                if t < 9 and t > 1:
                    res[k-1] = res[k] = str(t-1)
                if t == 0:
                    
            else:
                t= int(res[k])
                if t < 9 and t > 1:
                    res[k] = str(t-1)
        else:
            for i in range(k):
                res[-i-1] = res[i]
        return ''.join(res)
            