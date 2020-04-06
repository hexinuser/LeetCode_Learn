# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:32:20 2019

@author: Evan_He
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        res = [0,1]
        n,k = 2,1
        while n<= num:
            if n == 2**k:
                res.append(1)
                k += 1
            else:
                res.append(res[n%(2**(k-1))]+1)
            n += 1
        return res
"""  优化版本
class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        res = [0,1]
        k = 2
        for i in range(2,num+1):
            if n == k:
                res.append(1)
                k *= 2
                j = 1
            else:
                res.append(res[j]+1)
                j += 1
        return res
"""