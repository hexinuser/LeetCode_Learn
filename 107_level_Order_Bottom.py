# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:21:21 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stocks = [root]
        stock1 = []
        while True:
            node_res = []
            for stock in stocks:
                node_res.append(stock.val)
                if stock.left:
                    stock1.append(stock.left)
                if stock.right:
                    stock1.append(stock.right)
            if stock1:
                stocks,stock1 = stock1,[]
                res.append(node_res)
                node_res = []
            else:
                res.append(node_res)
                break
        return res[::-1]
