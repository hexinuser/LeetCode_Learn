# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:33:32 2019

@author: Evan_He
"""

class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil
        
        low,upper = ceil(sum(piles)/H), max(piles)
        while low < upper:
            mid = (low+upper)//2
            t = sum([ceil(pile/mid) for pile in piles])
            if t > H:
                low = mid+1
            else:
                upper = mid
        return low
        
        """
        k = math.ceil(sum(piles)/H)
        i = k
        while i >= k:
            h = sum([math.ceil(x/i) for x in piles])
            if h <= H:
                return i
            i += 1
        """