# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:45:56 2019

@author: Evan_He
"""

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        # 法一
        res = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[j] + 1,res[i])
        return max(res)
    
       #法二
        stack = [nums[0]]  
        for i in range(1,n):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                for j in range(len(stack)):
                    if nums[i] <= stack[j]:
                        stack[j] = nums[i]   #替换不影响最大长度只更改对应位置的比较
                        break
                #此处搜索满足元素的位置，可以采用二分法，因为stack为一个有序列表
        return len(stack) 
    
