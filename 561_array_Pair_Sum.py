# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:47:10 2018

@author: Evan_He
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])