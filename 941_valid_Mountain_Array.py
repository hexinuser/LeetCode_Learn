# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:45:34 2018

@author: Evan_He
"""

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False
        a = max(A)
        index = A.index(a)
        n = len(A)
        if index == 0 or index == n-1:
            return False
        for i in range(index):
            if A[i]>= A[i+1]:
                return False
        for i in range(index,n-1):
            if A[i]<= A[i+1]:
                return False
        return True