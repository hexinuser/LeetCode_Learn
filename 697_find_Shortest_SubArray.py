# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:35:49 2018

@author: Evan_He
"""
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        n = len(nums)
        nums_2 = nums[::-1]
        res = n
        count_dict = {}
        max_num = 0
        #for num in nums:
         #   count_dict[num] = count_dict.get(num,0)+1
          #  max_num = max(max_num,count_dict[num])
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 0
        max_num = max(count_dict.values())
        if max_num == 1:
            return 1
        for key,value in count_dict.items():
            if value == max_num:
                res = min(res,n-nums_2.index(key)-nums.index(key))
        return res
        """
        from collections import Counter
        nums_2 = nums[::-1]
        n = len(nums)
        res = n
        count_dict = Counter(nums)
        max_num = max(count_dict.values())
        if max_num == 1:  #防止度为1的极端情况
            return 1
        for key,value in count_dict.items():
            if value == max_num:
                res = min(res,n-nums_2.index(key)-nums.index(key))
        return res
            
        
        
        