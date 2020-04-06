# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:17:50 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def num_node(root1):
            left,right = [],[]
            if root1.left:
                left = num_node(root1.left)
            if root1.right:
                right = num_node(root1.right)
            return left+[root1.val]+right
        num = num_node(root)
        i,j = 0,len(num)-1
        while i<j:
            if k-num[i] > num[j]:
                i += 1
            elif k-num[i] == num[j]:
                return True
            else:
                j -= 1
        return False
            