# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:09:12 2018

@author: Evan_He
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)
        #A与B不同为1时，A、B的预算结果才为1，否则为0 (二进制) x^y^x = y
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
        """