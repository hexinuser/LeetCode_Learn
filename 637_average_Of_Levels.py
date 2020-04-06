# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:33:31 2018

@author: Evan_He
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        mean_floor = []
        nodes = [root]
        next_nodes = []
        while nodes:
            values = []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            mean_floor.append(sum(values)/len(values))
            nodes,next_nodes = next_nodes,[]
        return mean_floor