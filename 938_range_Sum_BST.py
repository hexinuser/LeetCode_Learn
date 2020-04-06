# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:24:55 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        t = root.val
        if t > R:
            return self.rangeSumBST(root.left, L, R)
        elif t < L:
            return self.rangeSumBST(root.right, L, R)
        elif t == L:
            return t + self.rangeSumBST(root.right, L, R)
        elif t == R:
            return t + self.rangeSumBST(root.left, L, R)
        else:
            return t + self.rangeSumBST(root.left, L, t) + self.rangeSumBST(root.right, t, R)
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""#修正，默认输入的L！= R, 减少判断，更快
class Solution(object): 
    def rangeSumBST(self, root, L, R):
        if not root or L == R:
            return 0
        t = root.val
        if t > R:
            return self.rangeSumBST(root.left, L, R)
        elif t < L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return t + self.rangeSumBST(root.left, L, t) + self.rangeSumBST(root.right, t, R)
"""    