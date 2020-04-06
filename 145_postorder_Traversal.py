# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:15:08 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        if not root:
            return []
        if not(root.left or root.right):
            return [root.val]
        result = self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result += [root.val]
        return result
        """
        if not root:
            return []
        stock = [root]
        res = []
        while stock:
            node = stock.pop()
            if type(node)!= TreeNode:
                res.append(node)
                continue
            left = node.left
            right = node.right
            stock.append(node.val)
            if right:
                stock.append(right)
            
            if left:
                stock.append(left)
        return res

        """
        if root is None:
            return []
        stack=[root]
        result=[]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1
        """

