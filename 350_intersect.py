# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:19:14 2018

@author: Evan_He
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ret = []
        for num1 in nums1:
            if num1 in nums2:
                nums2.remove(num1)
                ret.append(num1)
        return ret
            
            
            