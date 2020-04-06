# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:48:14 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        n = len(nums)//2
        res = TreeNode(nums[n])
        res.left = self.sortedArrayToBST(nums[:n])
        res.right = self.sortedArrayToBST(nums[n+1:])
        return res