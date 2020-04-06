# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:28:00 2019

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack_1, stack_2 = [root.left],[root.right]
        while stack_1:
            node1 = stack_1.pop()
            node2 = stack_2.pop()
            if node1:
                if not node2:
                    return False
                elif node1.val != node2.val:
                    return False
                else:
                    if node1.left and node2.right:
                        stack_1.append(node1.left)
                        stack_2.append(node2.right)
                    else:
                        if node1.left != node2.right:
                            return False
                    if node1.right and node2.left:
                        stack_1.append(node1.right)
                        stack_2.append(node2.left)
                    else:
                        if node2.left != node1.right:
                            return False
            else:
                if node2:
                    return False
        return True                              