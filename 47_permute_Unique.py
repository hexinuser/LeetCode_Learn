# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:35:52 2019

@author: Evan_He
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.uniq(nums)
    
    def uniq(self,nums):
        n = len(nums)
        if n == 0:
            return [[]]
        if len(set(nums)) == 1:
            return [nums]
        i = 1
        res = []
        right = self.permuteUnique(nums[1:])
        for r in right:
            res.append([nums[0]]+r)
        while i < n:
            if nums[i] == nums[i-1]:
                i += 1
                continue
            right = self.permuteUnique(nums[:i]+nums[i+1:])
            for r in right:
                res.append([nums[i]]+r)
            i += 1
        return res