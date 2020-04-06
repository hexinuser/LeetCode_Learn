# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:04:04 2018

@author: Evan_He
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True