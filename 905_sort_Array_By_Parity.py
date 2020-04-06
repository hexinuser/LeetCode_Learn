# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:43:16 2018

@author: Evan_He
"""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 对比可得，在尾部添加元素比在头部添加快很多
        """
        res = []
        for num in A:
            if num % 2 == 0:
                res = [num] + res
            else:
                res.append(num)
        return res
        """
        """
        odd = []
        even = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
        """
        # 原地交换，不产生新的数组
        i,j = 0,len(A)-1
        while i < j:
            if A[i] % 2 == 1:
                A[i],A[j] = A[j],A[i]
                j -= 1
            else:
                i += 1
        return A
        
        
        