# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:53:12 2018

@author: Evan_He
"""

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n<0:
            return self.myPow(1/x,-n)
        elif n == 0:
            return 1
        if n%2 == 0:
            return self.myPow(x,n//2)**2
        else:
            return self.myPow(x,n//2)**2*x
            