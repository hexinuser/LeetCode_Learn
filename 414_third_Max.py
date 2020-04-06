# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:41:57 2018

@author: Evan_He
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        b=c=None
        for i in range(1,len(nums)):
            if nums[i]>a:
                if b==None:
                    b=a
                else:
                    c=b
                    b=a
                a = nums[i]
            elif nums[i]<a:
                if b==None:
                    b = nums[i]
                elif b<nums[i]:
                    c=b
                    b = nums[i]
                elif nums[i]<b:
                    if c==None:
                        c=nums[i]
                    elif c<nums[i]:
                        c=nums[i]
                        
        if c==None:
            return a
        else:
            return c
                    
                        
                    
            