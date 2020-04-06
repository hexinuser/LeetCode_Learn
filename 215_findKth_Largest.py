# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:21:45 2019

@author: Evan_He
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]