# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:56:23 2018

@author: Evan_He
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%(n)
        
        if k!=0:
            nums[:k],nums[k:] = nums[-k:],nums[:-k]
        """
        i = 0
        
        while i< k :
            num =nums.pop()
            nums.insert(0,num)
            i += 1
        """