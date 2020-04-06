# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:10:42 2018

@author: Evan_He
"""

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while True:
            n = len(nums)//2
            if n==0:
                return(nums[0])
            if nums[n-1]!=nums[n] and nums[n+1]!=nums[n]:
                return(nums[n])
            else:
                if nums[n-1]==nums[n] and n%2==0:
                    nums=nums[:n-1]
                elif nums[n+1]==nums[n] and n%2!=0:
                    nums=nums[:n]
                    
                elif n%2==0:
                    nums=nums[n:]
                
                else:
                    nums=nums[n+1:]
        