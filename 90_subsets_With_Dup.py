# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:35:22 2019

@author: Evan_He
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        nums.sort()
        return self.deep_rec(nums)+[[]]
        
        
    def deep_rec(self,nums):
        n = len(nums)
        if n == 0:
            return [[]]
        i = 1
        res = [[nums[0]]]
        while i < n:
            if nums[i] == nums[i-1]:
                res.append(res[-1]+[nums[i]])
                i += 1
            else:
                break
        if i == n:
             return res
        else:
            ret = self.deep_rec(nums[i:])
        res_c = res.copy()
        for right in ret:
            for left in res_c:
                res.append(left+right)
            res.append(right)
        return res