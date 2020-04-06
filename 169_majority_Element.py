# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:40:12 2018

@author: Evan_He
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num)>n:
                return num
                