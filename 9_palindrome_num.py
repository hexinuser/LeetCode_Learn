# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:35:39 2018

@author: Evan_He
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        a=str(x)
        b=a[::-1]
        return b==a
        """
        x_bar = x
        if x<0:
            return False
        y = 0
        while True:
            t = x//10
            rem = x%10
            y+=rem
            if t>0:
                x = t
            else:
                break
            y = y*10
        return y==x_bar