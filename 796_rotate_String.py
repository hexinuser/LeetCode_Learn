# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:24:28 2018

@author: Evan_He
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if B in 2*A:
            return True
        return False
        """
        if len(A)!=len(B):
            return False
        A = list(A)
        for i in range(len(A)-1):
            A=A[1:]+A[0]
            if A==B:
                return True
        if A=='':
            return True
        return False
        """