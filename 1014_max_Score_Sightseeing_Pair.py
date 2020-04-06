# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:03:07 2019

@author: Evan_He
"""

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        #重构
        up_max= A[0]
        res = up_max+A[1]-1
        for k in range(len(A)-1):
            up_max = max(up_max,A[k]+k)
            res = max(res,up_max+A[k+1]-k-1)
        return res
        """
        #第二种代码的重构
        up_max,down_max= A[0],A[1]-1
        res = up_max+down_max
        k = 1
        while k<len(A)-1:
            up_max = max(up_max,A[k]+k)
            t = A[k+1]-k-1
            if t >= down_max:
                down_max = t
            res = max(res,up_max+t)
            k += 1
        return res
        """
        
        """原始版本
        n = len(A)
        A0 = [A[i]+i for i in range(n-1)]
        A1 = [A[j]-j for j in range(1,n)]
        up_max,down_max= A0[0],A1[0]
        res = up_max+down_max
        k = 1
        while k<n-1:
            up_max = max(up_max,A0[k])
            if A1[k] >= down_max:
                res = max(res,A1[k]+up_max)
                down_max = A1[k]
            else:
                res = max(res,up_max+A1[k])
            k += 1
        return res
        """