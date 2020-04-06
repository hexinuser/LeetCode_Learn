# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:09:07 2018

@author: Evan_He
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num ==0:
            return 0
        t = num%9
        if t == 0:
            return 9
        return t