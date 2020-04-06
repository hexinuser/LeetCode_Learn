# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:18:52 2018

@author: Evan_He
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)    
            else:
                j += 1
            
        """
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                   
        nums[j:] = [0]*(n-j)
        