# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:39:53 2018

@author: Evan_He
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        #计数重置
        k1 = nums.count(0)
        k2 = nums.count(1)
        n = len(nums)
        for i in range(n):
            if i <k1:
                nums[i] = 0
            elif i< k1+k2:
                nums[i] = 1
            else:
                nums[i] = 2
        """
        ##进行交换首尾
        k0 = 0
        k2 = len(nums)-1
        i = 0
        while i<=k2:
            if nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[i],nums[k2] = nums[k2],nums[i]
                k2 -= 1
            else:
                nums[i],nums[k0] = nums[k0],nums[i]
                k0 += 1
                i+=1
            
                
                
                
        
        