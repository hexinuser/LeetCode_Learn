# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:43:47 2019

@author: Evan_He
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        initial = 0
        bef = 1
        res = 0
        i,n = 0,len(nums)
        t = 0
        while i < n:
            bef *= nums[i]
            if bef < k:
                i += 1
                continue
            else:
                res += (i-initial)*(i+1-initial)//2-t*(t+1)//2
                t = i-initial
            while initial <= i:
                t -= 1
                bef //= nums[initial]
                initial += 1
                if bef >= k:
                    continue
                else:
                    break
            i += 1
        res += (i-initial)*(i+1-initial)//2-t*(t+1)//2
        return res