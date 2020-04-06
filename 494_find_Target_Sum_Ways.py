# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:38:42 2019

@author: Evan_He
"""
"""
原问题等同于： 找到nums一个正子集和一个负子集，使得总和等于target

我们假设P是正子集，N是负子集 例如： 假设nums = [1, 2, 3, 4, 5]，target = 3，一个可能的解决方案是+1-2+3-4+5 = 3 这里正子集P = [1, 3, 5]和负子集N = [2, 4]

因此，原来的问题已转化为一个求子集的和问题： 找到nums的一个子集 P，使得sum(P) = (target + sum(nums)) / 2
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_n = sum(nums)
        if (sum_n+S)%2!=0 or sum_n<S:
            return 0
        return self.sub_set(nums,(S+sum_n)//2)
        
    def sub_set(self,nums,S):
        dp = [0]*(S+1)
        dp[0] = 1
        for num in nums:
            #每一遍循环得到和值为i的方法数，以次更新
            for i in range(S,num-1,-1):
                dp[i] += dp[i-num]
        return dp[S]
    
        """ 递归求解，超时
        if (sum(nums)+S)%2!=0:
            return 0
        if len(nums) == 1:
            if nums[0] == abs(S):
                if S == 0:
                    return 2
                return 1
            else:
                return 0
        return self.findTargetSumWays(nums[:-1],S+nums[-1])+self.findTargetSumWays(nums[:-1],S-nums[-1])
        """