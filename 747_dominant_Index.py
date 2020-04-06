# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:30:46 2018

@author: Evan_He
"""

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        t = nums.index(a)
        nums.remove(a)
        if nums==[]:
            return 0
        if a>=2*max(nums):
            return t
        return -1