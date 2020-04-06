# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:26:34 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        stock = [root]
        stock_next = []
        while True:
            for node in stock:
                if node.left:
                    stock_next.append(node.left)
                    res += 1
                else:
                    return res
                if node.right:
                    stock_next.append(node.right)
                    res += 1
                else:
                    return res
            stock = stock_next
            stock_next =[]
            