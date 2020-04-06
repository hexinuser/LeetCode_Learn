# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:22:38 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        t = 1
        stack=[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left  #左边遍历到底
            node=stack.pop()
            if t == k:
                return node.val
            cur=node.right
            t += 1
