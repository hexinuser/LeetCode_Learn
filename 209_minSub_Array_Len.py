# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:20:13 2019

@author: Evan_He
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        k,res,sum_i = -1,n+1,0
        for i in range(n):
            sum_i += nums[i]
            if sum_i >= s:
                while sum_i-nums[k+1] >= s:
                    sum_i -= nums[k+1]
                    k += 1
                res = min(res,i-k)
        if res == n+1:
            return 0
        else:
            return res