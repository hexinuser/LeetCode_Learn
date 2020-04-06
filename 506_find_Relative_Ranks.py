# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 23:37:29 2018

@author: Evan_He
"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        """
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return ['Gold Medal']
        if n==2:
            if nums[0]<nums[1]:
                return ['Silver Medal','Gold Medal']
            else:
                return ['Gold Medal','Silver Medal']
        num_sort = sorted(nums)
        res = [str(n - num_sort.index(num)) for num in nums]
        res[res.index('1')] = 'Gold Medal'
        res[res.index('2')] = 'Silver Medal'
        res[res.index('3')] = 'Bronze Medal'
        return res
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        arr = sorted(list(enumerate(nums)), key=lambda x: x[1])
        for i in range(len(nums)):
            index = arr.pop()[0]
            if i < 3:
                nums[index] = medals[i]  
            else:
                nums[index]	= str(i+1)	
        return nums