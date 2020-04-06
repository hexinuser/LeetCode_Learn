# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:07:14 2019

@author: Evan_He
"""

class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """ 
        #错位相减，增加的是项和，去除最后一位及其权重
        n = len(A)
        sum0, sum_A = 0, 0
        for i in range(n):
            sum0 += i*A[i]
            sum_A += A[i]
        res, res_mid = sum0, sum0
        for j in range(1,n+1):
            res_mid += sum_A - n*A[-j]
            if res_mid > res:
                res = res_mid
        return res