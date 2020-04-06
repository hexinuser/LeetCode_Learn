# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:29:07 2019

@author: Evan_He
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        min_index = self.find_min(nums)
        if nums[-1]<target:
            return self.find_tar(nums[:min_index], target)
        else:
            t =  self.find_tar(nums[min_index:], target)
            if t == -1:
                return -1
            else:
                return min_index+t                         
           
    def find_tar(self, nums, target):
        i,j = 0,len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1
    
    
    def find_min(self,nums):
        if nums[-1] > nums[0]:
            return 0
        i,n = 0,len(nums)-1
        num = nums[-1]
        while i <= n:
            mid = (i+n)//2
            if nums[mid] < num:
                if nums[mid-1] > nums[mid]:
                    return mid
                n = mid-1
            else:
                if nums[mid+1] < nums[mid]:
                    return mid+1
                i = mid+1
        return mid
        