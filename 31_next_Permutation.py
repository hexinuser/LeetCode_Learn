# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:39:03 2019

@author: Evan_He
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        max_num = nums[-1]
        sign = True
        for i in range(2,n+1):
            t = nums[-i]
            if t >= max_num:
                max_num = t
            else:
                sign = False
                j = -i+1
                while j < 0:
                    if nums[j] <= t:
                        break
                    j += 1
                break
        if sign:
            nums.reverse()
        else:
            nums[-i],nums[j-1] = nums[j-1],nums[-i]
            nums[-i+1:] = nums[-i+1:][::-1]