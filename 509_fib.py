# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:45:37 2019

@author: Evan_He
"""

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        F0 , F1 = 0 , 1
        k = 2
        while k <= N:
            F0,F1 = F1,F0+F1
            k += 1
        return F1