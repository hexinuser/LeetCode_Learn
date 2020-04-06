# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:07:33 2018

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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        pre =[root.val]
        children = root.children
        for child in children:
            pre += self.preorder(child)
        return pre
        