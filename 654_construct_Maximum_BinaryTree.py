# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:15:32 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """#递归
        if nums == []:
            return None
        max_num = max(nums)
        index = nums.index(max_num)
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        return node
        """
        #循环
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack and num < stack[-1].val:
                stack[-1].right = node
            stack.append(node)
        return stack[0]