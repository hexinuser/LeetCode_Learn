# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 23:48:50 2018

@author: Evan_He
"""

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) != len(A):
                return True
            else:
                return False
        else:
            res = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    res.append(i)
            if len(res) == 2:
                if A[res[0]] == B[res[1]] and A[res[1]] == B[res[0]]:
                    return True
            return False