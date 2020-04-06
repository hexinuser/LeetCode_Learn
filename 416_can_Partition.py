# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:35:43 2019

@author: Evan_He
"""

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #递归超时
        def findNum(numL,s):
            if s==0:
                return True
            if numL == []:
                return False
            else:
                for i in range(len(numL)):
                    if numL[i] > s:
                        continue
                    if findNum(numL[i+1:],s-numL[i]):
                        return True
                return False
        
        sum_num = sum(nums)
        if sum_num%2 == 1:
            return False
        t = sum_num//2
        if t < max(nums):
            return False
        nums.sort(reverse=True)
        return findNum(nums,t)
