# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:56:34 2018

@author: Evan_He
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """##暴力法
    
        n = len(nums)
        for i in range(1,n):
            if k!=0:
                a = [sum(nums[j:j+i+1])%k for j in range(n-i)]
            else:
                a = [sum(nums[j:j+i+1]) for j in range(n-i)]
            if 0 in a:
                return True
        return False
        """
        
        """sum(nums[:j]) % k == sum(nums[:i]) % k for j-i>=2, 判断和的余数是否相等，字典下标"""
        n = len(nums)
        if n <= 1:
            return False
        model = {0:-1}
        sum_n = 0
        for index,num in enumerate(nums):
            if k!=0:
                sum_n  = (sum_n+num)%k
            else:
                sum_n += num
            if sum_n in model:
                if index-model[sum_n]>1:
                    return True
            else:
                model[sum_n] = index
        return False
        
