# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:34:09 2018

@author: Evan_He
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n==1:
            return [nums]
        if n == 0:
            return [[]]
        res = []
        for i in range(n):
            num_lists = self.permute(nums[:i]+nums[i+1:])
            for num in num_lists:
                res.append([nums[i]]+num)
        return res