# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:56:48 2018

@author: Evan_He
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        """ min L-W, s.t. L>=W; L*W =area"""
        L = area
        W,k = 1,1
        mid = int(area**(0.5))
        while k <= mid:
            if area%k==0:
                L = int(area//k)
                W = k
            k += 1
        return [L,W]