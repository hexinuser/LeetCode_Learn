# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:46:18 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        if not root:
            return []
        result = [root.val]
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result
        """
    
        if not root:
            return []
        stock = [root]
        res = []
        while stock:
            node = stock.pop()
            res.append(node.val)
            left = node.left
            right = node.right
            if right:
                stock.append(right)
            if left:
                stock.append(left)
        return res
       