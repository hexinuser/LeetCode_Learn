# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:37:38 2018

@author: Evan_He
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        index = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[index]=nums[i]
                index +=1
        return index
                