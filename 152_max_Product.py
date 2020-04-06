# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:45:08 2019

@author: Evan_He
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mid = [0,0]
        if nums[0] >= 0:
            mid = [0,nums[0]]
        else:
            mid = [nums[0],0]
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                mid[1] = max(nums[i],nums[i]*mid[1])
                mid[0] = mid[0]*nums[i]
            else:
                mid[0],mid[1] = min(nums[i],nums[i]*mid[1]), nums[i]*mid[0]
            res = max(res,mid[1])
        return res