# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:56:46 2019

@author: Evan_He
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]