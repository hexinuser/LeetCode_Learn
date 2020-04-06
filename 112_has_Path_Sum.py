# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:38:09 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        l,r=False,False
        if root.left:
            l = self.hasPathSum(root.left,sum-root.val)
        if root.right:
            r = self.hasPathSum(root.right,sum-root.val)
        return l or r