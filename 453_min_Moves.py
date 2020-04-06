# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:30:26 2018

@author: Evan_He
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """#时间复杂度太高
        if len(set(nums)) == 1:
            return 0
        max_num,min_num = max(nums),min(nums)
        i,sub = nums.index(max_num), max_num-min_num
        nums = [num+sub for num in nums]
        nums[i] -= sub
        return sub+self.minMoves(nums)
        """ 
        """
        min_num = min(nums)
        return sum([num-min_num for num in nums] )
        """
        return sum(nums) - min(nums)*len(nums)