# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:28:58 2018

@author: Evan_He
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #n = max(A)
        #return A.index(n)
        
        a,b = 0,len(A)
        i = (a+b)//2
        while True:
            if A[i]>=A[i+1]:
                b = i
            else:
                a = i
            if b- a <=1:
                if A[a]>A[b]:
                    return a
                else:
                    return b
            else:
                i = (a+b)//2