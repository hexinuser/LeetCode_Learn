# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:08:29 2019

@author: Evan_He
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threeSum(nums,target):
            n = len(nums)
            res = []
            i = 0
            while i <= n-3:
                if i > 0 and nums[i] == nums[i-1]:
                    i += 1
                    continue
                j = i+1
                k = n-1
                while j < k:
                    t = nums[i]+nums[j]+nums[k]
                    if t == target:
                        res.append([nums[i],nums[j],nums[k]])
                        while nums[j]==nums[j+1]:
                            j += 1
                            if j >= k:
                                break
                        while nums[k-1]==nums[k]:
                            k -= 1
                            if k <= j:
                                break
                        j += 1 
                        k -= 1
                    elif t > target:
                        while nums[k-1]==nums[k]:
                            k -= 1
                            if k <= j:
                                break
                        k -= 1
                    else:
                        while nums[j]==nums[j+1]:
                            j += 1
                            if j >= k:
                                break
                        j += 1
                i += 1
            return res
        res = []
        nums.sort()
        n = len(nums)-4
        t = 0
        while t <= n:
            if t > 0 and nums[t] == nums[t-1]:
                t += 1
                continue
            res0 = threeSum(nums[t+1:],target-nums[t])
            while res0:
                res.append([nums[t]]+res0.pop())
            t += 1
        return res