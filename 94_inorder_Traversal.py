# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:45:37 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        if not root:
            return []
        result = self.inorderTraversal(root.left)
        result += [root.val]
        result += self.inorderTraversal(root.right)
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
            if right:
                stock.append(right)
            stock.append(node.val)
            if left:
                stock.append(left)

        return res
        """
        if root is None:
            return []
        stack=[]
        result=[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left  #左边遍历到底
            node=stack.pop()
            result.append(node.val)
            cur=node.right
            
        return result
        """
