# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:36:51 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        sign = 0
        res = []
        stock = [root]
        stock_next = []
        while stock:
            res_node = []
            if sign:
                while stock:
                    node = stock.pop()
                    res_node.append(node.val)
                    if node.right:
                        stock_next.append(node.right)
                    if node.left:
                        stock_next.append(node.left)
                res.append(res_node)
                res_node = []
                stock,stock_next = stock_next,[]
                sign = 0
            else:
                while stock:
                    node = stock.pop()
                    res_node.append(node.val)
                    if node.left:
                        stock_next.append(node.left)
                    if node.right:
                        stock_next.append(node.right)
                res.append(res_node)
                res_node = []
                stock,stock_next = stock_next,[]
                sign = 1
        return res
        
""" #简化版本

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        sign = 1
        res = []
        stock = [root]
        stock_next = []
        while True:
            res_node = []
            while stock:
                node = stock.pop()
                res_node.append(node.val)
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
            res.append(res_node)
            res_node = []
            if not stock_next:
                return res
            stock,stock_next = stock_next,[]
            sign = 1-sign
"""