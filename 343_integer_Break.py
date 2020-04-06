# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:21:29 2018

@author: Evan_He
"""

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ##分离的数不会超过4
        if n==2:
            return 1
        if n==3:
            return 2
        t1=int(n/3)
        t2=n-t1*3
        if t2==0:
            return 3**t1
        elif t2==1:
            return 3**(t1-1)*4
        else:
            return 3**t1*t2
        