# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:44:45 2019

@author: Evan_He
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        if len(nums) == 2:
            return nums[::-1]
        res = [nums[0]]
        for i in range(1,len(nums)):
            res.append(res[-1]*nums[i])
        res[-1],res[-2] = res[-2],res[-3]*nums[-1]
        for j in range(2,len(nums)-1):
            nums[-j] *= nums[-j+1]
            res[-j-1] = res[-j-2]*nums[-j]
        res[0] = nums[1] *nums[2]
        return res
    
    """
        n = len(nums)
        if n == 2:
            return nums[::-1]
        res = [1]
        for i in range(n-1):
            res.append(res[-1]*nums[i])
        p = 1
            
        for j in range(-2,-n-1,-1):
            p *= nums[j+1]
            res[j] *= p
        return res