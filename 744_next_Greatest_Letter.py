# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:17:33 2019

@author: Evan_He
"""

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left,right = 0, len(letters)
        while left<right:
            mid = (left+right)//2
            if letters[mid] <= target:
                left = mid+1
            elif letters[mid]>target:
                right = mid
                if mid == 0:
                    return letters[0]
                elif letters[mid-1]<=target:
                    return letters[mid]
        return letters[0]