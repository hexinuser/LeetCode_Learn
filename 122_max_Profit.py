# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:47:04 2018

@author: Evan_He
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(prices)):
            t = prices[i]-prices[i-1]
            if t>0:
                count += t
        return count
                