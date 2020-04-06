# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:58:56 2018

@author: Evan_He
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0,len(numbers)-1
        while left < right:
            t = numbers[left]+numbers[right]
            if t == target:
                return [left+1,right+1]
            elif t < target:
                left += 1
            else:
                right -= 1
            