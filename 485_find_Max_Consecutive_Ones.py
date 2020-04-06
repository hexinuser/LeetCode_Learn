# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:14:51 2018

@author: Evan_He
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """#字符串形式求解
        nums = ''.join(map(str,nums))
        n = len(nums)
        i = nums.find('0')
        if i == -1:
            return n
        res = i
        while i<n-1:
            j =  nums.find('0',i+1)
            if j==-1:
                res = max(res,n-i-1)
                break
            else:
                res = max(res,j-i-1)
                i = j
        return res
        """
        res = 0
        i,n = 0,len(nums)
        while i < n:
            count = 0
            while nums[i] == 1:
                count += 1
                i += 1
                if i >= n:
                    break
            res = max(count,res)
            i += 1
        return res