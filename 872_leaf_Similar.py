# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:18:01 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return leaf(root.left) + leaf(root.right)
        
        return leaf(root1) == leaf(root2)