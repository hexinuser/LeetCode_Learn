# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:32:16 2018

@author: Evan_He
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left , right= 0, n
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            sign = guess(mid)
            if sign == 0:
                return mid
            elif sign == 1:
                left = mid+1
            else:
                right = mid-1

        