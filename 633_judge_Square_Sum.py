# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:06:35 2018

@author: Evan_He
"""

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c==0:
            return True
        n = int(c**0.5)
        for i in range(n+1):
            t = (c-i**2)**0.5
            if int(t)==t:
                return True
        return False