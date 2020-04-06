# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:48:12 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        import math 
        if root == None:
            return []
        res = [root.val]
        stack1 = [root]
        stack2 = []
        while True:
            max_num = -math.inf
            while stack1:
                node = stack1.pop()
                if node.left:
                    stack2.append(node.left)
                    if node.left.val>max_num:
                        max_num = node.left.val
                if node.right:
                    stack2.append(node.right)
                    if node.right.val>max_num:
                        max_num = node.right.val
            if max_num > -math.inf:
                res.append(max_num)
            if stack2 == []:
                return res
            stack1,stack2 = stack2,[]
