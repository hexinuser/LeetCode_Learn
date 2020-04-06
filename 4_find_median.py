# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:54:07 2018

@author: Evan_He
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2) 
        if m > n:  #假设n>=m
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        """ 
        总长度的一半 N
        A  [0,1...i-1]  [i...m-1]
        B  [0,1...j-1]  [j...n-1]  n>=m
        i+j = (m + n + 1) // 2 二分查找
        满足A[i-1]<=B[j] 且A[i]>=B[j-1]
        """
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]: #选择A的右半部分 重新划分
            # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, must decrease it
                imax = i - 1
            else: #划分i成功，处理边界
            # i is perfect

                if i == 0: 
                    max_of_left = nums2[j-1]
                elif j == 0: 
                    max_of_left = nums1[i-1]
                else: 
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else: 
                    min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2