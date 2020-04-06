# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:54:52 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = [root.val]
        while True:
            stack1 = []
            for node in stack:
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            stack = stack1.copy()
            if not stack:
                return res
            res.append(stack[-1].val)
        