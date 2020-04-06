# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:22:08 2018

@author: Evan_He
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        #暴力法，超时, 时间复杂度O(n^3)
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[k] > abs(nums[i]-nums[j]) and nums[k] < nums[i]+nums[j]:
                        res += 1
        return res
        """
        """ #j,k同时循环，时间复杂度O(n^2)
        def count_tri(num,n):
            res_0 = 0
            j,k= 1,2 
            while j < n-1:
                t = num[0]+num[j]
                while k < n:
                    if num[k] < t:
                        k += 1
                    else:
                        break
                res_0 += k-j-1
                j += 1
                if j==k:
                    k += 1
            return res_0
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            res += count_tri(nums[i:],n-i)
        return res
        """
        #第二种算法的改良，平均复杂度O(n^2),(第二种相当于对每个n都有2*n次循环)
        nums.sort()
        nums.reverse()
        n,res = len(nums),0
        for i in range(0,n-2):
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    res+=(right-left)
                    left+=1
                else:
                    right-=1
        return res

            
            
                
            