# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:07:08 2018

@author: Evan_He
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))