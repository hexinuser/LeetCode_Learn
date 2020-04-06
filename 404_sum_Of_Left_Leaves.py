# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:32:59 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is  None:
            return 0
        sum_left = self.sumOfLeftLeaves(root.right)
        left = root.left
        if left:
            if not (left.left or left.right):
                sum_left +=left.val
            else:
                sum_left += self.sumOfLeftLeaves(left)
 
        return sum_left
            