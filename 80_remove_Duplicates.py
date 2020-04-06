# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:04:19 2018

@author: Evan_He
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ #正向和反向两种
        n = len(nums)
        j = 1
        while j < n-1:
            if nums[-j] == nums[-j-1]:
                while nums[-j-1] == nums[-j-2]:
                    nums.pop(-j)
                    n -= 1
                    if j+2 > n:
                        break
                    continue
                j += 2
            else:
                j += 1
        return n
        """
        index=0
        for num in nums:
            if index<2 or num>nums[index-2]:
                nums[index]=num
                index+=1
        return index
        """