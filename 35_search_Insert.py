# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:41:48 2018

@author: Evan_He
"""

Vclass Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """ #适用于未排序好的数组
        try:
            return nums.index(target)
        except:
            count = 0
            for num in nums:
                if num < target:
                    count += 1
            return count
        """
        """
        #二分法1
        try:
            return nums.index(target)
        except:
            left,right = 1,len(nums)-1
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return right+1
            mid = (left+right)//2
            while left<=right:
                if nums[mid] < target:
                    if nums[mid+1] > target:
                        return mid+1
                    else:
                        left = mid+1
                if nums[mid] > target:
                    if nums[mid-1] < target:
                        return mid
                    else:
                        right = mid
                mid = (left+right)//2
        """
        #二分法二
        left,right = 0,len(nums)
        while left<right:
            mid = (left+right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        return right