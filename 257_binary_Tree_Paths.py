# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:06:15 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        val = str(root.val)
        res = []
        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        for path in paths:
            res.append(val+'->'+path)
        if not res:
            res = [val]
        return res