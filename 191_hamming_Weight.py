# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:15:32 2018

@author: Evan_He
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')