# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:13:41 2018

@author: Evan_He
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        mean = [sum(nums[:k])/k]
        n = len(nums)
        for i in range(1,n-k+1):
            mean.append(mean[-1]+(nums[i+k-1]-nums[i-1])/k)
        return max(mean)