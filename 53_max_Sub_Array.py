# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:05:17 2019

@author: Evan_He
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        i,n = 0,len(nums)
        while i < n:
            if nums[i]>0:
                res = nums[i]
                t = res
                break
            res = max(res,nums[i])
            i += 1
        for j in range(i+1,n):
            t = max(t+nums[j],0)
            res = max(t,res)
        return res