# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:26:38 2018

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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        nodes = [root]
        children=[]
        while nodes:
            floor = []
            for node in nodes:
                floor.append(node.val)
                children += node.children
            
            nodes,children=children,[]
            res.append(floor)
        return res