# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:20:16 2018

@author: Evan_He
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        left,right = 1, n
        while left<right:
            mid = (left+right)//2
            sign = isBadVersion(mid)
            if sign:
                right = mid  
            else:
                left = mid+1
                
        return left