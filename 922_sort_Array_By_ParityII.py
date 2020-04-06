# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:04:13 2018

@author: Evan_He
"""

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i,j = 0,1
        res = A.copy()
        for num in A:
            if num % 2 == 0:
                res[i] = num
                i += 2
            else:
                res[j] = num
                j += 2
        return res