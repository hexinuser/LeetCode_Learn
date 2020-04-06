# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:49:39 2018

@author: Evan_He
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        t = A[-1] - A[0]
        if t == 0:
            return len(set(A)) == 1
        elif t > 0:
            for i in range(len(A)-1):
                if A[i+1] < A[i]:
                    return False
            return True
        else:
            for i in range(len(A)-1):
                if A[i+1] > A[i]:
                    return False
            return True