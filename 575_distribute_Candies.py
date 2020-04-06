# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:13:29 2018

@author: Evan_He
"""

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)//2,len(set(candies)))
   