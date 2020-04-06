# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:02:28 2018

@author: Evan_He
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ #不使用递归，可减少搜索深度
        if not root:
            return 0
        now_node = [root]
        child_node =[]
        depth = 1
        while now_node:
            for node in now_node:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    child_node.append(node.left)
                if node.right:
                    child_node.append(node.right)
            depth+=1
            now_node,child_node = child_node,[]

        """#利用递归，代码简洁，但会搜索到最大深度
        if not root:
            return 0
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if left*right==0:
                return 1+left+right
            else:
                return 1+min(left,right)
            
        """