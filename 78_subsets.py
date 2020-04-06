# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:28:47 2019

@author: Evan_He
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[]
        n=len(nums)
        for i in range(2**n):
            si=bin(i)[2:]
            result=[]
            for i in range(len(si)):
                if si[i]=='1':
                    result.append(nums[i-len(si)])
            results.append(result)
        return results
                
            