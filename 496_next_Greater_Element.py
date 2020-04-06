# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:03:44 2018

@author: Evan_He
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        big_num2 = []
        i = 0
        n = len(nums2)
        while i < n :
            j = i+1
            while j < n:
                if nums2[j] > nums2[i]:
                    big_num2.append(nums2[j])
                    break
                j += 1
            if j == n:
                big_num2.append(-1)
            i += 1
        res = []
        for num in nums1:
            res.append(big_num2[nums2.index(num)])
        return res
        