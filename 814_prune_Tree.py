[2,7,9,3,1]# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:08:11 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        if not root.left and not root.right:
            if root.val == 0:
                return None
        left,right = None,None
        if root.left:
            left = self.pruneTree(root.left)
        if root.right:
            right = self.pruneTree(root.right)
        if left == None and right == None:
            if root.val == 1:
                return TreeNode(1)
            else:
                return None
        else:
            root.left = left
            root.right = right
            return root