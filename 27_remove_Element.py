# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:39:42 2018

@author: Evan_He
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """
        count=0
        for i in range(len(nums)):
            if nums[i]==val:
                count+=1
            else:
                nums[i-count]=nums[i]
        return len(nums)-count
        """
        k1 = 0
        k2 = len(nums)-1
        while k1<=k2:
            if nums[k1]==val:
                nums[k1],nums[k2] = nums[k2],nums[k1]
                k2 -= 1
            else:
                k1 += 1
        return k2+1