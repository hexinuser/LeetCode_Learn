# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:48:04 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))