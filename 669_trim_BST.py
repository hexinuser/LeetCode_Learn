# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:15:44 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        #二叉搜索树，左边元素值小于根节点，右边大于根节点
        def trim(node):
            if not node:
                return None
            if node.val > R:
                node = trim(node.left)
            elif node.val < L:
                node = trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node
        return trim(root)