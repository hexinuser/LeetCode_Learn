# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:59:44 2018

@author: Evan_He
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if root.children == None:
            return 1
        else:
            children = root.children
            depth = 0
            for child in children:
                depth = max(depth,self.maxDepth(child))
            return depth + 1 
        