# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:58:54 2019

@author: Evan_He
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        if j == -1:
            return 1
        while i < j:
            if nums[i] <= 0 or nums[i]-1 >= j:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
            else:
                if nums[i]-1 == i:
                    i += 1
                elif nums[i]-1<i:
                    nums[i] = nums[j]
                    j -= 1
                else:
                    if nums[i] == nums[nums[i]-1]:
                        nums[i]= nums[j]
                        j -= 1
                    else:
                        t = nums[i]-1
                        nums[i],nums[t]= nums[t],nums[i]
        for k in range(len(nums)):
            if nums[k] != k+1:
                return k+1
        return k+2