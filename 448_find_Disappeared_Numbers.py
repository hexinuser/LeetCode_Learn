# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:05:47 2018

@author: Evan_He
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1,len(nums)+1))-set(nums))