# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:27:31 2019

@author: Evan_He
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)
        r1,r2 = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            r = max(r2,r1+nums[i])
            r1,r2 = r2,r
        return r
        """
        if nums == []:
            return 0
        if len(nums)<=2:
            return max(nums)
        if len(nums)==3:
            return max(nums[1],nums[0]+nums[2])
        return max(nums[0]+self.rob(nums[2:]),nums[1]+self.rob(nums[3:]))
        """