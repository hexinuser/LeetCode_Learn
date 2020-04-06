# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 00:06:17 2018

@author: Evan_He
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        save_dict = {}
        res = []
        for num in nums:
            save_dict.setdefault(num,0)
            save_dict[num] += 1
        for key,value in save_dict.items():
            if value == 1:
                res.append(key)
        return res
        
        