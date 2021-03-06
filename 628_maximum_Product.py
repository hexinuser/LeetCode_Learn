# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:20:26 2019

@author: Evan_He
"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        return max(nums[0]*nums[1]*nums[2],nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])