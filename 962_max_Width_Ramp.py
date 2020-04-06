# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:39:23 2019

@author: Evan_He
"""

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = sorted(list(range(len(A))),key=lambda x: A[x] )
        res,low = 0,len(B)
        for i in B:
            res = max(i-low,res)
            low = min(i,low)
        return res
        
        """利用栈,先找到递减序列
        res = 0
        n = len(A)
        stack = []
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        while i > res:
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack.pop())
            i -= 1
        return res
        """