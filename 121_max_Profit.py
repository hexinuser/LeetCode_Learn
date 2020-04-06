# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:33:14 2018

@author: Evan_He
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        if not prices:
            return 0
        res = []
        i,n,buy = 0,len(prices),None
        while i < n-1:
            if prices[i] <  prices[i+1]:
                buy = prices[i]
                i += 1
                break
            i += 1
        if buy==None:
            return 0
        while i < n-1:
            if prices[i] >= prices[i+1]:
                res.append(prices[i]-buy)
            else:
                buy = min(buy,prices[i])
            i += 1
        res.append(prices[i]-buy)
        return max(res)
        """
        #简化版
        if not prices:
            return 0
        res = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                res = max(res,prices[i]-buy)
        return res