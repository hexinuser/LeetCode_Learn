# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:30:59 2018

@author: Evan_He
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]        
         """       

        n=len(nums)
        for i in range(n-1):
            b = target  - nums[i]
            try :
                j = nums[i+1:n].index(b)
                return [i,j+i+1]
            except:
                pass
        
        dic = {}
        for index,value in enumerate(nums):
            #判断键值是否存在，直接用 in (has_key()为python2的代码，python3改为__contains__(key), in dic.keys()最慢)
#            if target-value in dic.keys():
#            if target-value in dic:
            if dic.__contains__(target-value):
                return [dic[target - value],index]
            else:
                dic[value] = index
        
a= Solution()

print(a.twoSum([2,7,11,15],9))