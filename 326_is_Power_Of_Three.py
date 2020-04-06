# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:49:42 2018

@author: Evan_He
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        import math
        if n<=0:
            return False
        t = math.log(n,3)
        
        return 3**round(t)==n
        """
        if n<=0:
            return False
        return 3**20%n==0  #32为精度最大的数为2**32，而3**21次方已经超出