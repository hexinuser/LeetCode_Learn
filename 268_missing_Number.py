# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:17:14 2018

@author: Evan_He
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        n=max(nums)
        if n!=len(nums):
            return n+1
        else:
            return list(set(range(n+1))-set(nums))[0]
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)