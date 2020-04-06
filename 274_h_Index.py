# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:57:08 2019

@author: Evan_He
"""

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """ #对数阶
        b = sorted(citations)
        k , n = 0 , len(citations)
        res = 0
        for i in range(1,n+1):
            while k < n:
                if b[k] >= i:
                    break
                k += 1
            if k == n:
                break
            if min(i,n-k) >= res:
                res = min(i,n-k)
            else:
                return res
        return res
        """
        #线性阶，可优化最后两次的代码，只遍历一次
        n = len(citations)
        if n == 0:
            return 0
        res = [0]*n
        for num in citations:
            if num >= n:
                res[-1] += 1
            elif num > 0:
                res[num-1] += 1
        h = 0
        for i in range(2,n+1):
            res[-i] += res[-i+1]
        for j in range(n):
            if h <= min(j+1,res[j]):
                h = min(j+1,res[j])
            else:
                return h
        return h
                
                
        