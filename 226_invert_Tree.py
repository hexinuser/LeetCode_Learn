# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:13:39 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root