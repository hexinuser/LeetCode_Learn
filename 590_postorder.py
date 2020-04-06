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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        if not root:
            return []
        last =[root.val]
        children = root.children
        n = len(children)
        for i in range(1,n+1):
            child = children[-i]
            last = self.postorder(child)+last
        return last
        """
        if not root:
            return []
        last = []
        stack = [root,]
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            last.append(node.val)
        return last[::-1]
        
        