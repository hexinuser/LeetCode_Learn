# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:09:03 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val ==val:
                return root
            elif root.val <val:
                root = root.right
            else:
                root = root.left
        return None