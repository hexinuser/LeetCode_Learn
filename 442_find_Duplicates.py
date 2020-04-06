# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:03:31 2018

@author: Evan_He
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """# 字典存储
        result = []
        res = {}
        for num in nums:
            res[num] = res.get(num, 0)+1
            if res[num] > 1:
                result.append(num)
        return result
        """
        """
        #set存储
        result = []
        res = set()
        for num in nums:
            if num not in res:
                res.add(num)
            else:
                result.append(num)
        return result
        """
        """#利用库的计数包计算
        from collections import Counter
        res = []
        count = Counter(nums)
        for key,value in count.items():
            if value >1:
                res.append(key)
        return res
        """ #不使用额外空间，如果一个num出现两次，那么nums[num]的值在第二次乘以-1的时候回变回正数
        res = [] 
        for num in nums:
            num = abs(num)
            nums[num-1] *= -1
            if nums[num-1]>0:
                res.append(num)
        return res
        