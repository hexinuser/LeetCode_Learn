# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:09:46 2019

@author: Evan_He
"""

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fin = [1]
        nums = [str(1)]
        for i in range(2,n+1):
            fin.append(fin[-1]*i)
            nums.append(str(i))
        fin.pop()
        res = ''
        while k > 1:
            fin_l = fin.pop()
            t,k = k//fin_l,k%fin_l
            if k == 0:
                res += nums[t-1]
                nums.remove(nums[t-1])
                return  res+''.join(nums[::-1])
            res += nums[t]
            nums.remove(nums[t])
        return res+''.join(nums)