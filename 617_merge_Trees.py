# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:27:07 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if not t1:
            return t2  
        if not t2:
            return t1
        res = TreeNode(t1.val+t2.val)
        res.left = self.mergeTrees(t1.left,t2.left)
        res.right = self.mergeTrees(t1.right,t2.right)
        return res
    
        """可简写为
        if t1 and t2:
            res = TreeNode(t1.val+t2.val)
            res.left = self.mergeTrees(t1.left,t2.left)
            res.right = self.mergeTrees(t1.right,t2.right)
            return res
        else:
            return t1 or t2
        """