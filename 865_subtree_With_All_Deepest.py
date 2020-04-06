# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:58:04 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def count_deep(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            else:
                return 1+max(count_deep(node.left),count_deep(node.right))
        
        d1,d2 = count_deep(root.left),count_deep(root.right)
        if d1 == d2:
            return root
        elif d1 > d2:
            return self.subtreeWithAllDeepest(root.left)
        else:
            
            return self.subtreeWithAllDeepest(root.right)
            