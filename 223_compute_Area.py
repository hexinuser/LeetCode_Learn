# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:06:59 2018

@author: Evan_He
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S = (C-A)*(D-B)+(G-E)*(H-F)
        
        x = sorted([A,C,E,G])
        y = sorted([B,D,F,H])
        
        if B>=H or D<= F:
            return S
        if C<=E or A>=G:
            return S
        return S- (x[2]-x[1])*(y[2]-y[1])