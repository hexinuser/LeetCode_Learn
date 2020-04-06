# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:50:40 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stock = [root]
        stock_next = []
        sign = 1
        res1=res2=root
        while True:
            while stock:
                node = stock.pop()
                if sign:
                    if node.left:
                        stock_next.append(node.left)
                    if node.right:
                        stock_next.append(node.right)
                else:
                    if node.right:
                        stock_next.append(node.right)
                    if node.left:
                        stock_next.append(node.left)
            
            if not stock_next:
                if sign:
                    return res2.val
                else:
                    return res1.val
            else:
                sign = 1-sign  
                stock = stock_next
                res1,res2 = stock[0],stock[-1]
                stock_next = []