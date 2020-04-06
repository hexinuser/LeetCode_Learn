# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:08:44 2018

@author: Evan_He
"""

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        #self.sum = [sum(self.nums[:i+1]) for i in range(len(self.nums))]
        self.sum = [0]
        for i in range(len(self.nums)):
            self.sum.append(self.sum[-1]+self.nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #return sum(self.nums[i:j+1])
        #return self.sum[j]-self.sum[i] +self.nums[i]
        
        return self.sum[j+1]-self.sum[i]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)