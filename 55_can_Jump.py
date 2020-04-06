# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:28:33 2019

@author: Evan_He
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-2
        if n == -1:
            return True
        k = n+1
        while n >= 0:
            if nums[n]+n >= k:
                k = n
            n -= 1
        return k == 0
                
            
            
        