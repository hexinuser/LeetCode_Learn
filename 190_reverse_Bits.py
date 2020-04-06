# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:57:01 2018

@author: Evan_He
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = bin(n)[2:]
        lenth = len(bin_n)
        bin_n = '0'*(32-lenth)+bin_n
        return int(bin_n[::-1],2)