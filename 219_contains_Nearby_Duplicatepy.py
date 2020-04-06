# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:14:13 2019

@author: Evan_He
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res_dict = {}
        for i in range(len(nums)):
            if nums[i] in res_dict:
                if k >= i-res_dict[nums[i]]:
                    return True
                else:
                    res_dict[nums[i]] = i
            else:
                res_dict[nums[i]] = i
        return False