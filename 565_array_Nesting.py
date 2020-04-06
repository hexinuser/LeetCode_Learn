# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:45:15 2019

@author: Evan_He
"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        index = set(range(len(nums)))
        while index:
            old = index.pop()
            mid = 1
            new = nums[old]
            while new != old :
                index.remove(new)
                new = nums[new]
                mid += 1
            res = max(res,mid)
            if len(index)<=res:
                return res
        return res