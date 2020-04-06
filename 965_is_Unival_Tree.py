# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:40:21 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        val = root.val
        stock = [root]
        while stock:
            node = stock.pop()
            if node.val != val:
                return False
            if node.left:
                stock.append(node.left)
            if node.right:
                stock.append(node.right)
        return True